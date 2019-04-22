#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calc(*numbers):
    sums = 0
    for n in numbers:
        sums = sums + n*n
    return sums


def product(*x):
    s = 1
    for n in x:
        s = s * n
    return s


print(calc(5, 8, 9, 12, 15))
c = [2, 4, 7, 9, 12]
print(calc(*c))
print(product(5, 10, 20, 31, 54))

