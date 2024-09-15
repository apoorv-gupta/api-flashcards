This is a collection of String utilities that are useful for solving algorithm problems. 
Java strings are immutable. Each character is an unsigned 16 bit value. A Codepoint is a Unicode symbol. It may take multiple characters to represent a character: https://stackoverflow.com/a/23980051

The Interface CharSequence is implemented by CharBuffer, Segment, String, StringBuffer & StringBuilder
String Templates were cancelled in JDK 23.

## Other advanced classes:
https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/text/package-summary.html


## Recently added methods
from https://javaalmanac.io/jdk/23/apidiff/17/
* StringBuffer
    * repeat(CharSequence, int)
    * repeat(int, int)

* StringBuilder
    * repeat(CharSequence, int)
    * repeat(int, int)

* String
    * indexOf(String, int, int)
    * indexOf(int, int, int)
    * splitWithDelimiters(String, int)
