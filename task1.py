#!/usr/bin/env python

n = int(input("N:"))

if (n >= 0) and (n >= 1) and (n <= 20):
    for i in range(n):
        print(i * i)
else:
    print(n, "is incorrect number")
