#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'Bob': 56, 'helen': 98, 'Tracy': 96}
print(d['Bob'])
print(d)
d['job'] = 99
print(d)
i = d.get('jack', -2)
j = d.get('helen', -1)
print(i, j)
d.pop('Tracy')
print(d)
