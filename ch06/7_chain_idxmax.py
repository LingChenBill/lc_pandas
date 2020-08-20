#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/8/19
# @Author: Lingchen
# @Prescription: 用链式方法重现idxmax(page_155)
import pandas as pd
import numpy as np

college = pd.read_csv('../data/college.csv', index_col='INSTNM')
cols = ['MD_EARN_WNE_P10', 'GRAD_DEBT_MDN_SUPP']

for col in cols:
    college[col] = pd.to_numeric(college[col], errors='coerce')

college_n = college.select_dtypes(include=[np.number])
criteria = college_n.nunique() == 2
binary_cols = college_n.columns[criteria].tolist()
college_n = college_n.drop(labels=binary_cols, axis='columns')
print(college_n.max().head())

print('college_n.max() 可以选出每列的最大值，用eq方法比较DataFrame的每个值和该列的最大值：')
print(college_n.eq(college_n.max()).head())

print('用any方法，选出至少包含一个True值的行：')
has_row_max = college_n.eq(college_n.max()).any(axis='columns')
print(has_row_max.head())

print('因为只有18列，has_row_max 最多只能有18个True,来看下实际共有多少个：')
print(college_n.shape)
print(has_row_max.sum())

print(college_n.eq(college_n.max()).cumsum())
print(college_n.eq(college_n.max()).cumsum().cumsum())

print('现在就可以用eq方法去和1进行比较，然后用any方法，选出所有至少包含一个True值的行：')
has_row_max2 = college_n.eq(college_n.max())\
                        .cumsum()\
                        .cumsum()\
                        .eq(1)\
                        .any(axis='columns')
print(has_row_max2.head())

print('查看有多少个True值：')
print(has_row_max2.sum())

print('直接通过布尔索引选出这些学校：')
idxmax_cols = has_row_max2[has_row_max2].index
print(idxmax_cols)

print('和idxmax方法的结果比较：')
print(set(college_n.idxmax().unique()) == set(idxmax_cols))



