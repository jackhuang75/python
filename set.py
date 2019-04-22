#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from function import my_abc
s = set([1, 2, 3])
print(s)
s.add(4)
print(s)
s.remove(1)
print(s)
s2 = {4, 5, 6, 7}
print(s & s2)
print(s | s2)
a = ['y', 'd', 'h', 'u']
a.sort()
print(a[3])
b = set([1, 2, 3, 4, 5, 6])
print(b)
print(my_abc(-99))
