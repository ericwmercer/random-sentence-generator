Random Sentence Generator
=========================
Computer-generated [Mad Libs](http://en.wikipedia.org/wiki/Mad_Libs)

Overview
--------
This was my third programming assignment for CS101 (Intro to Computer Science). The goal was to implement a variant of Mad Libs where the computer is given a story template and then randomly fills in the blanks from a set of suggested words/phrases according to a pre-defined set of rules. I was given starter code in the form of a view-controller module called ``rsgSimpleLauncher.py``, a sample grammar file ``apt-issues.g``, and a skeleton model module called ``rsgModel.py`` whose functions I needed to implement using what I'd recently learned in class about pattern-matching and recursion so that the computer would know how to process a grammar file specifying the story parameters.

More specifically, the computer is given a grammar file that contains a set of definitions (each enclosed by curly braces and named by the non-terminal in angled brackets on the first line within) and rules for each definition (the semicolon-separated lines following the non-terminal). Random text is then generated beginning with the non-terminal ``<start>`` by randomly replacing each subsequent nonterminal with one of the rules provided by its definition - which can sometimes reference other definitions or recursively reference their own definition - until all nonterminals have been processed. At this point the computer then prints out the full randomly-generated story.

Instructions
------------
Place your grammar files in the  ``src/`` directory (see ``apt-issues.g`` for an example) and then run ``python rsgSimpleLauncher.py``. When prompted, enter the number corresponding to the current grammar file for which you'd like to generate random text. Repeat as desired by entering "y". Alternatively, enter "n" to choose a different grammar to use or exit the program by entering "-1". 

Sample Output
-------------
```
$ python rsgSimpleLauncher.py 
choose one of the grammars below by entering its number:
 
0   apt-issues.g
enter number (-1 to exit)>  0
opening  apt-issues.g
text generation started
I am still working on this week's APT assignment. 
The problems were like easy .  
repeat with same grammar?>[y/n] y
opening  apt-issues.g
text generation started
I am still working on this week's APT assignment. 
The problems were like impossible and Eclipse 
crashed .  
repeat with same grammar?>[y/n] n
choose one of the grammars below by entering its number:
 
0   apt-issues.g
enter number (-1 to exit)>  -1
thanks for using RSG
```
