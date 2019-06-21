#!/usr/bin/env python

inpstr = input("string:")
rdystr = inpstr.replace(" ", "")
strlen = len(rdystr) - 1
curpos = 0

while (curpos <= strlen - curpos):

    if rdystr[curpos] != rdystr[strlen - curpos]:
        print(inpstr, "is NOT palindrome")
        quit()
    curpos += 1

print(inpstr, "is palindrome")
