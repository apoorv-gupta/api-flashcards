from bs4 import BeautifulSoup
import csv
import os


def extract(f):
  soup = BeautifulSoup(f, 'html.parser')
  b = soup.body
  cards = []
  for table in b.find_all('table',  class_ = "summary-table"):
      trs = table.tbody.find_all('tr')
      for tr in trs:
          card = [soup.head.title.get_text().partition(" ")[0]]
          for col in tr.children:
              if str(type(col)) != '<class \'bs4.element.Tag\'>':
                  continue
              card.append(col.get_text().replace("\n", " ").replace(";", ","))
          if len(card) == 4:
            card = [card[0], card[1] + " " + card[2], card[3]]
          card = [card[0]+"::"+card[1], card[0] + "::" + card[2]]
          cards.append(card)

  return cards

def load(cards):
  os.makedirs('./generated/', mode = 0o777, exist_ok = True)
# TODO: this is the name of the output file, which should be replaced if you are not interested in collection_framework
  with open('./generated/collections.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvwriter .writerows(cards)

def main():
  cards = []
# TODO: this is the input file, which should be replaced if you are not interested in collection_framework
  with open("collection_framework/included", "r") as classnames:
    for classname in classnames.readlines():
        filename = os.path.join(os.path.join(os.path.expanduser("~") ,"Downloads/docs/api/java.base/"), classname[:-1])
        with open(filename, "r") as f:
          cards.extend(extract(f))
        
  load(cards)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
