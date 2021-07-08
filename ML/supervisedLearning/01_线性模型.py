#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 线性模型 https://scikit-learn.org.cn/view/4.html

# 1 、普通最小二乘法

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
reg.coef_
# array([0.5, 0.5])

# 2、回归
reg = linear_model.Ridge(alpha=.5)
reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
# Ridge(alpha=0.5)
reg.coef_
# array([0.34545455, 0.34545455])
reg.intercept_
# 0.13636...

# 3、分类

