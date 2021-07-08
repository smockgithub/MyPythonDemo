#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#可以通过使用 Python 的内置持久化模块（即 pickle ）将模型保存:
# 请注意，pickle 有一些安全性和维护性问题。
from sklearn import svm
from sklearn import datasets
# from sklearn import datasets

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)

# 它能够实现任意对象与文本之间的相互转化，也可以实现任意对象与二进制之间的相互转化。也就是说，pickle 可以实现 Python 对象的存储及恢复。
# 不仅限于SVC()，可以用于任何对象，转换为str存储在txt/db，使用时再取出来用。
import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0:1])

print(y[0])

# pickle 模块提供了以下 4 个函数供我们使用：
# dumps()：将 Python 中的对象序列化成二进制对象，并返回；
# loads()：读取给定的二进制对象数据，并将其转换为 Python 对象；
# dump()：将 Python 中的对象序列化成二进制对象，并写入文件；
# load()：读取指定的序列化数据文件，并返回对象




# 在scikit的具体情况下，使用 joblib 替换 pickle（ joblib.dump & joblib.load ）可能会更有趣，这对大数据更有效，但只能序列化 (pickle) 到磁盘而不是字符串变量
from joblib import dump, load
# joblib.dump 以及 joblib.load 函数也接受 file-like（类文件） 对象而不是文件名。
dump(clf, 'filename.joblib') # 持久化到根目录filename.joblib这个文件

clf3 = load('filename.joblib')
print(1)