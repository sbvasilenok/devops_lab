#!/usr/bin/env python

splsnt = input("sentence:").split()
wrdlst = [item[::-1] for item in splsnt]
print(" ".join(wrdlst))
