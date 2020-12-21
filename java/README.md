The program reads the API docs for all the pages listed in the included file and creates an output CSV file.

You can then create a new Deck in Anki by importing that CSV file. It is recommended to create two Anki cards for each line:
* With method name, arguments and return value as the question and the rest as answer
* With method description and runtime complexity as the question and the rest as answers

TODO: Add API runtime information 


Instructions:
* Download Anki: https://apps.ankiweb.net/
* Download the JDK documentation for Java 15 from  https://stackoverflow.com/questions/6986993/how-to-download-javadoc-to-read-offline in ~/Downloads and unzip it
* Read the README.md and the included file in the directory you are interested in (collection_framework, streams etc)
* Update javadoc_etl.py to refer to the correct included file and update the name of the output CSV file
* Run "python3 javadoc_etl.py" on the shell
* You'll find a new generated/ folder that contains the new csv file.
* Open Anki > File > Import. Select the CSV file from the previous step and create a new Anki Deck.
