#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = int(input('请输入你的年龄：'))
if age >= 18:
    print('you age is', age)
    print('adult')
elif age >= 6:
    print('你的年龄是：', age)
    print('teenager')
else:
    print('你的年龄是：', age)
    print('kid')
