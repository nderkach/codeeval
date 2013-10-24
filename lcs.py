#!/usr/bin/python

import sys

#recursive O(2**n) solution
def lcsRec(x, y):
    if x and y:
        xa, xb = x[:-1], x[-1]
        ya, yb = y[:-1], y[-1]
        # check if strings have a common last character
        if xb == yb:
            return lcsRec(xa, ya) + xb
        else:
            return max(lcsRec(xa, y), lcsRec(x, ya), key=len)
    else:
        # basecase, check if one if the strings is null
        return ""

def lcs(str):
    # test for empty line
    if not str.strip():
        return False        
    l = str.split(';')
    # test for the correct string format
    assert len(l) == 2

    s1, s2 = l
    if not 0 < (len(s1) or len(s2)) < 50:
        return False;

    return lcsRec(s1, s2)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print "Usage: ./lcs.py [input_file]"
        print "Input file should contain two strings per line, semicolon delimited."
        sys.exit()
    file = open(sys.argv[1], 'r')
    for line in file.read().splitlines():
        res = lcs(line)
        if (res):
			print res

