The program reads the API docs for all the pages listed in the included file and creates an output CSV file.

You can then create a new Deck in Anki by importing that CSV file. It is recommended to create two Anki cards for each line:
* With method name, arguments and return value as the question and the rest as answer
* With method description and runtime complexity as the question and the rest as answers

TODO: Add API runtime information 

## Updating the code:
* If the HTML for the Java pages has changed, the output of this python file could break. Use:
    * Phind or another engine to write the bs4 code to extract the methods information
    * https://yoksel.github.io/html-tree/en/ to understand the HTML
* Make sure you glance at the output files to do sanity testing. Sometimes, the code fails silently over parsing errors

## Running the code:
* You can use pythonanywhere.com to get a free Linux server to update & run these scripts

## Resources for learning Java:
* https://github.com/matyb/java-koans
* Recent functions: https://javaalmanac.io/jdk/23/apidiff/21/
* https://dev.java: launched in 2021; haven’t used it yet. Is it good?
* Language enhancements: https://advancedweb.hu/new-language-features-since-java-8-to-21/
* TODO: build a java project using modules or buck2 or gradle etc, maybe one of https://aosabook.org/en/
* TODO: OOPS in Java
* TODO: Generics
* Learning adanced concepts: go through code review comments or stack overflow questions

## Creating an Anki Deck:
* Download Anki: https://apps.ankiweb.net/
* Find current Java version supported by CodePair, Hackerrank & CodeSignal (let's say 21)
    * https://support.codesignal.com/hc/en-us/articles/360039872514-What-languages-can-I-use
* Download the JDK documentation for Java 21
    * from  https://stackoverflow.com/questions/6986993/how-to-download-javadoc-to-read-offline in ~/Downloads
    * unzip jdk-21.0.4_doc-all.zip "docs/api/java.base/*"
* Read the README.md and the included file in the directory you are interested in (collection_framework, streams etc)
* Update javadoc_etl.py to refer to the correct included file and update the name of the output CSV file
* Run "python3 javadoc_etl.py" on the shell
* You'll find a new generated/ folder that contains the new csv file.
* Open Anki Desktop -> create deck  > File > Import. Select the CSV file from the previous step 
    * select Import options -> notetype -> Basic & reversed . Select the columns for front, back & tag.
    * Set up Fast SRS by following  https://github.com/open-spaced-repetition/fsrs4anki/blob/main/docs/tutorial.md
    * Open a deck. Go to options >  FSRS > Desired retention to 0.8
