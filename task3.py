#!/usr/bin/env python

w, h = [int(i) for i in input("w: h: ").split()]
sqr = [[0] * h for i in range(w)]
fill = 0

for n in range(int(input("n: "))):
    x1, y1, x2, y2 = [int(i) for i in input("x1: y1: x2: y2: ").split()]

    for x in range(x1, x2):
        for y in range(y1, y2):

            if sqr[x][y] == 0:
                fill += 1

            sqr[x][y] = 1

print("blank square", w * h - fill)
