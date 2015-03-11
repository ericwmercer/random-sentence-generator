'''
Created on Nov 8, 2010

@author: ola
'''

import rsgModel
import os
rootdir = "."

def getChoice():
    """
    Choose a grammar and return the filename
    return None to signal done
    """
    names = []
    num = 0
    print "choose one of the grammars below by entering its number:\n "
    for f in os.listdir(rootdir):
        if f.endswith(".g"):
            print "%d\t%s" % (num,f)
            num += 1
            names.append(f)
    
    print "enter number (-1 to exit)> ",
    choice = int(raw_input())
    if 0 <= choice < len(names):
        return names[choice]
    return None

def getYesNo(prompt):
    choice = 'x'
    while not choice in ['y','n']:
        print prompt+"[y/n]",
        choice = raw_input()
        choice = choice.lower()
    return choice

def prompt():
    
    choice = getChoice()
    while choice:
        print "opening ",choice
        rsgModel.initialize(choice)
        rsgModel.start()
        repeat = getYesNo('repeat with same grammar?>')
        if repeat != 'y':
            choice = getChoice()
            
    print "thanks for using RSG"
        
prompt()
