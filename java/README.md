The program reads the API docs for all the pages listed in the included file and creates an output CSV file.

You can then create a new Deck in Anki by importing that CSV file. It is recommended to create two Anki cards for each line:
* With method name, arguments and return value as the question and the rest as answer
* With method description and runtime complexity as the question and the rest as answers

TODO: Add runtime complexity information for each method

## Tricks for Anki
* Press @ to suspend the current Anki card. It won't show up again until you manually select it. This is useful for duplicate or low-value cards
* 

## Updating the code:
* If the HTML for the Java pages has changed, the output of this python file could break. Use:
    * Phind or another engine to write the bs4 code to extract the methods information
    * https://yoksel.github.io/html-tree/en/ to understand the HTML
* Make sure you glance at the output files to do sanity testing. Sometimes, the code fails silently over parsing errors

## Running the code:
* You can use pythonanywhere.com to get a free Linux server to update & run these scripts

## Basic algorithms
* The String, Scanner, StringBuilder classes are very useful and take care of messy string parsing.
* Arrays and Collections classes. You can create a filtered deck on Anki to revise just these two. All methods are tagged by the name of the class
* High quality Java algorithms: https://web.archive.org/web/20221024063836/https://code-library.herokuapp.com/
* https://github.com/topics/competitive-programming?l=java   


## Ramping up on algorithms
* [Fixing common mistakes](https://docs.google.com/document/d/1KGccByc1-cKkL9jymzNFlAg1EnxjxivEaOulF0jrj5c/edit?tab=t.0)
* [Selected algorithms](https://www.youtube.com/playlist?list=PL6mp57-ykmTF1I2zZp3UAaNH3v8GWq97X)
  * Coin Changing Number of ways to get total dynamic programming
  * Maximum Sub Square Matrix Dynamic Programming
  * Numbers Without Consecutive 1s in binary representation
  * String Interleaving Dynamic Programming
  * Check if Binary Tree is Binary Search Tree
  * Maximum Rectangular Area in Histogram  
* https://cpbook.net/
* https://mattjhall.co.uk/posts/skiplists.html

## Other useful Java classes:
* Definitely learn how to read and write text to console
* [Objects class](https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/Objects.html#deepEquals(java.lang.Object,java.lang.Object))
* [Integer class](https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/lang/Integer.html)
* Double
* BigInteger
* Regex
* Scanner & PrintWriter
* Math
* StrictMath
* [Google’s Guava library is mostly obsolete](https://www.reddit.com/r/java/comments/13w2l8w/guava_320_released_today_and_the_beta_annotation/)
  * Used prolifically: Immutable collections, Multimaps
  * Used frequently:
    * Splitter/Joiner,
    * CharMatcher,
    * Preconditions,
    * Lists.partition,
    * Suppliers.memoize,
    * Ints/Longs.tryParse,
    * Resources,
    * MoreObjects.firstNonNull


## Resources for learning Java:
* Recent functions: https://javaalmanac.io/jdk/23/apidiff/21/
* https://dev.java: launched in 2021; haven’t used it yet. Is it good?
  * https://dev.java/learn/records/
* Language enhancements: https://advancedweb.hu/new-language-features-since-java-8-to-21/
* [Abridged Incomplete: Java for C++ programmers](https://docs.google.com/document/d/1WXG837hIIWbIVe08RvzV9YK5SpoHCXOXOwMrQepFinM/edit?tab=t.0)
* [Java Lessons] (https://docs.google.com/document/d/1KSEgPnucbOfxQaSH4Mif6hmItnKiv3gukEu5vnUeOUE/edit?tab=t.0)
* [Basic Java Notes from Educative](https://docs.google.com/document/d/1rd-BJSbApiJUJYwsp1e6tmKGbVRy-Cas1SgXK8IYJ8s/edit?tab=t.0#heading=h.mva67s26b0ui)
* TODO: OOPS in Java
* TODO: Generics
* Learning advanced concepts: go through code review comments or stack overflow questions

## Resources for practicing Java:
* https://github.com/matyb/java-koans
* https://exercism.org/tracks/java
* https://adventofcode.com/2024 has puzzles
* TODO: build a java project using modules or maven or gradle etc, maybe the graph database from https://aosabook.org/en/

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
 

