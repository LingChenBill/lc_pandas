#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/14
# @Author: Lingchen
# @Prescription: 比较缺失值
import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

# 使用Numpy NaN对象表示缺失值，不等于自身的特殊对象
print(np.nan == np.nan)

# Python的None对象是等于自身的
print(None == None)

college = pd.read_csv('../data/college.csv', index_col='INSTNM')
college_ugds = college.filter(like='UGDS_')
print(college_ugds.head())

# college_ugds所有值和.0019比较，返回布尔值DataFrame
print(college_ugds.head() == .0019)

# DataFrame和DataFrame比较
college_self_compare = college_ugds == college_ugds
print(college_self_compare.head())

# 用all()检查是否所有的值都是True:这是因为缺失值不互相等于
print(college_self_compare.all())

# 可以用 == 号判断，然后求和
print((college_ugds == np.nan).sum())

# 统计缺失值最主要方法是使用isnull方法
print(college_ugds.isnull().sum())

# 统计两个DataFrame最直接的方法是使用equals方法
# None，不是True
print(assert_frame_equal(college_ugds, college_ugds))

print(college_ugds.eq(.0019).head())

