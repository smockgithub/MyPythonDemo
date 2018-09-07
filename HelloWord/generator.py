#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)

next(g)
