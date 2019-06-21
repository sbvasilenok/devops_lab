#!/usr/bin/env python

n, m = [int(i) for i in input("n: m: ").split()]

setarrn = set([int(i) for i in input("n_integers: ").split()])
setarrA = set([int(i) for i in input("A_integers: ").split()])
setarrB = set([int(i) for i in input("B_integers: ").split()])

print(len(setarrn & setarrA) - len(setarrn & setarrB))
