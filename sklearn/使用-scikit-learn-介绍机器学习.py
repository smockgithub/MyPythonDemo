#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://sklearn.apachecn.org/#/docs/68?id=%E4%BD%BF%E7%94%A8-scikit-learn-%E4%BB%8B%E7%BB%8D%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0

from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

print("iris=",iris)
print("digits=",digits)

# digits.data digits.target


