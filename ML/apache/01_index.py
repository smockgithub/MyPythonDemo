#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard scientific Python imports
import matplotlib.pyplot as plt

# https://sklearn.apachecn.org/docs/master/51.html
# 官方教程

# 加载示例数据集
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

from sklearn import svm
# 分类器（classifier）
clf = svm.SVC(gamma=0.001, C=100.) #调参数，我们手动设置 gamma 值。不过，通过使用 网格搜索 及 交叉验证 等工具，可以自动找到参数的良好值。

# 作为一个训练集，让我们使用数据集中除最后10张以外的所有图像。 
clf.fit(digits.data[:-10], digits.target[:-10])  # 训练模型

# yc = clf.predict(digits.data[-1:]) # 预测 数据集的最后一个

for i in range(1,11):
    plt.subplot(2, 5, i) # 2行5列的第一个格子
    yc = clf.predict(digits.data[-i:])
    plt.title('shu: %d' %yc[0])
    plt.imshow(digits.images[-i])

#plt.figure()

plt.show()


print(1)
#input("输入任何数退出")