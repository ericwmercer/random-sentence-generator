'''
Created on Nov 7, 2010

@author: ericmercer
'''

import re,random

grammar = {}
text = ""

def initialize(filename):
    """
    Prepares a properly formatted text file to be used as a grammar for
    generating random text.
    """
    file = open(filename)
    allText = file.read()
    changedText = re.sub(r"\s+"," ",allText)
    gram = r"\{(.)+?\}"
    for m in re.finditer(gram, changedText):
        handle(m.group())
    file.close()

def handle(rule):
    """
    Builds a grammar in which each definition (non-terminal) is associated
    with a list of its rules.
    """
    global grammar
    pattern = r"\{\s*(\<(.)+?\>)(.*)\}"
    mat = re.match(pattern, rule)
    if mat:
        nont = mat.group(1).strip()
        remainder = mat.group(3)
        partPattern = r"((.)+?);"
        for mat in re.finditer(partPattern,remainder):
            production = mat.group(1)
            if nont in grammar:
                grammar[nont].append(production)
            else:
                grammar[nont] = [production]
    else:
        print rule,"doesn't match"

def start():
    """
    Generates random text by calling generateFrom() and prints it according to
    the specifications of printText(). Resets the grammar and string of random
    text at the end so as to enable repeated random generation.
    """
    print "text generation started"
    global grammar, text
    generateFrom("<start>")
    printText(text)
    grammar = {}
    text = ""

def generateFrom(rule):
    """
    Builds a string by randomly choosing a rule for each definition referenced
    in the non-terminal "<start>" and adding it. Coded to be recursive in order
    to deal with definitions that have non-terminal rules.
    """
    global grammar, text
    randomrule = random.choice(grammar[rule])
    for word in randomrule.split():
        if word.startswith("<"):
            generateFrom(word)
        else:
            text += word + " "
         
def printText(text):
    """
    Prints randomly generated text while wrapping the printout so as to keep
    lines at 50 characters or less with words kept intact (not split in half
    between lines).
    """
    line = ""
    for word in text.split(" "):
        if len(line + word) > 50:
            print line
            line = ""
        line += word + " "
    print line

