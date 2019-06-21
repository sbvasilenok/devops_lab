#!/usr/bin/env python

n = int(input("n:"))
w = len(str(bin(n)[2:])) - 1

for i in range(1, n + 1):
    print(f'{i:^{w}d}', f'{i:^{w}o}', f'{i:^{w}X}', f'{i:^{w}b}')
