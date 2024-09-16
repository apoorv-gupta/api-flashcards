from bs4 import BeautifulSoup
import csv
import os


def extract(f):
  soup = BeautifulSoup(f, 'html.parser')
  class_name = soup.head.title.get_text().partition(" ")[0]
  # Find the main container
  container = soup.find('div', id='method-summary-table')
  cards = []

  if container:
    # Extract table headers
    headers = container.select('.table-header')

    # Extract method information rows
    methods = container.select('.col-first, .col-second, .col-last')

    def extract_method_signature(method_element):
        method_name = method_element.text.strip().replace('\n', ' ')
        method_params = method_element.find('code')
        # Handle cases where there's no code element
        if method_params:
            full_method = f"{method_name}({method_params.text.strip()})"
        else:
            full_method = method_name
        return method_name


    # Print the extracted data
    for i in range(0, len(methods), 3):
        return_type = extract_method_signature(methods[i])
        if (return_type == 'Modifier and Type'):
            continue
        method = extract_method_signature(methods[i+1])
        description = methods[i+2].text.strip().replace('\n', ' ')
        method_prompt = class_name + "::" + return_type + " " + method
        method_description = class_name + "::" + description
        cards.append([method_prompt, method_description, class_name])
  else:
    print("No method summary table found in " + class_name)
  return cards


def load(cards):
  os.makedirs('./generated/', mode = 0o777, exist_ok = True)
# TODO: this is the name of the output file, which should be replaced if you are not interested in collection_framework
  with open('./generated/collections.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # https://docs.ankiweb.net/importing/text-files.html
    csvwriter.writerows(cards)

def main():
  cards = []
# TODO: this is the input file, which should be replaced if you are not interested in collection_framework
  included_libraries = "collection_framework/included"
  with open(included_libraries, "r") as classnames:
    print('found file ' + included_libraries)
    for classname in classnames.readlines():
        filename = os.path.join(os.path.join(os.path.expanduser("~") ,"Downloads/docs/api/java.base/"), classname[:-1])
        with open(filename, "r") as f:
          print('found file ' + filename)
          cards.extend(extract(f))
        
  load(cards)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
