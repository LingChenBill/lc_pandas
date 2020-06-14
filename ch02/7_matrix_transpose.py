#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/14
# @Author: Lingchen
# @Prescription: 矩阵转置
import pandas as pd

college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds = college.filter(like='UGDS_')
print(college_ugds.head())

# count()返回非缺失值的个数
print(college_ugds.count())

# axis默认为0
print(college_ugds.count(axis=0))

# 等价于axis = 'index'
print(college_ugds.count(axis='index'))

# 统计每行的非缺失值个数
print(college_ugds.count(axis='columns').head())

# 求和加以确认
print(college_ugds.sum(axis='columns').head())

# 用中位数了解每列的分布
print(college_ugds.median(axis='index'))

# 使用累积求和cumsum()可以很容易看到白人、黑人和西班牙裔的比例
print(college_ugds.cumsum(axis=1).head())

# UGDS_HISP一列降序排列
print(college_ugds.sort_values('UGDS_HISP', ascending=False))
