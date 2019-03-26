#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://sklearn.apachecn.org/#/docs/68?id=%E4%BD%BF%E7%94%A8-scikit-learn-%E4%BB%8B%E7%BB%8D%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0

from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

#print("iris=",iris)
print("digits=",digits.data)

# digits.data digits.target

from sklearn import svm

clf = svm.SVC(gamma=0.001, C=100.) #估计器Estimator，分类器（classifier）的一种
clf.fit(digits.data[:-1], digits.target[:-1])  
# SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
#  decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
#  max_iter=-1, probability=False, random_state=None, shrinking=True,
#  tol=0.001, verbose=False)

 # 我们把我们的估计器实例命名为 clf ，因为它是一个分类器（classifier）。它现在必须拟合模型，也就是说，它必须从模型中 learn（学习） 。 这是通过将我们的训练集传递给 fit 方法来完成的。作为一个训练集，让我们使用数据集中除最后一张以外的所有图像。 我们用 [:-1] Python 语法选择这个训练集，它产生一个包含 digits.data 中除最后一个条目（entry）之外的所有条目的新数组

clf.predict(digits.data[-1:])

import matplotlib.pyplot as plt
plt.figure(1,figsize=(3,3))
plt.imshow(digits.images[-1],cmap=plt.cm.gray_r,interpolation='nearest')
#plt.imshow(clf.predict(digits.data[-1:]))
plt.show()





