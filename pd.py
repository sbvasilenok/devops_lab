#!/usr/bin/env python


def palyndrome_detect(string):

    rdystr = str(string).replace(" ", "")
    strlen = len(rdystr) - 1
    curpos = 0

    while (curpos <= strlen - curpos):

        if rdystr[curpos] != rdystr[strlen - curpos]:
            print(string, "is NOT palindrome")
            return False
        curpos += 1

    print(string, "is palindrome")
    return True
