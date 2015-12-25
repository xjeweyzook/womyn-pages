#!/bin/python2
from sys import argv

def main():
    print "\x1b[2J\x1b[H" + argv[1].upper()+"(1)\t\tLinux User's Manual"
    print "NAME"
    #bullshit goes here
    print "SYNOPSIS"
    #bullshit goes here
    print "DESCRIPTION"
    #bullshit goes here
    print "OPTIONS"

if __name__ == "__main__":
    main()
