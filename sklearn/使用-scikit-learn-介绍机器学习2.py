#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型持久化 pickle

from sklearn import svm,datasets
clf=svm.SVC()
iris=datasets.load_iris()
x,y=iris.data,iris.target
clf.fit(x,y)

import pickle
s=pickle.dumps(clf)
clf2=pickle.loads(s)
clf2.predict(x[0:1])
y[0]


# \underset{w}{min\,} {|| X w - y||_2}^2
