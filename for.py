#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['jack', 'cake', 'joe', 'helen']
for name in names:
    print(name)
su = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    su = su + x
print(su)
sm = 0
for x in range(101):
    sm = sm + x
print(sm)
count = 0
n = 99
while n > 0:
    count = count + n
    n = n - 2
print(count)
L = ['Bart', 'Lisa', 'Adam']
n = 0
while n <= 2:
    print('你好：', L[n], '!')
    n = n+1
print('end')
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('end')
n = 0
while n <= 10:
    n = n+1
    if n % 2 == 0:
        continue
    print(n)
print('end')
