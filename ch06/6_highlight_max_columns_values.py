#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/8/18
# @Author: Lingchen
# @Prescription: 高亮每列的最大值（page_151）
import pandas as pd
import numpy as np

pd.options.display.max_rows = 6
college = pd.read_csv('../data/college.csv', index_col='INSTNM')
print(college.dtypes)

print('MD_EARN_WNE_P10 和 GRAD_DEBT_MDN_SUPP 两列是对象类型，对其进行检查，发现含有字符串：')
print(college.MD_EARN_WNE_P10.iloc[0])
print(college.GRAD_DEBT_MDN_SUPP.iloc[0])

print('降序检查：')
print(college.MD_EARN_WNE_P10.sort_values(ascending=False).head())

print('可以用 to_numeric ，将某列的值做强制转换：')
cols = ['MD_EARN_WNE_P10', 'GRAD_DEBT_MDN_SUPP']
for col in cols:
    college[col] = pd.to_numeric(college[col], errors='coerce')

print(college.dtypes.loc[cols])

print('用 select_dtypes 方法过滤出数值列：')
college_n = college.select_dtypes(include=[np.number])
print(college_n.head())

print('有的列只含有两个值，用 nunique() 方法挑出这些列：')
criteria = college_n.nunique() == 2
print(criteria.head())

print('将布尔 Series 传给索引运算符，生成二元列的列表：')
binary_cols = college_n.columns[criteria].tolist()
print(binary_cols)

print('用 drop 方法删除这些列：')
college_n2 = college_n.drop(labels=binary_cols, axis='columns')
print(college_n2.head())

print('用 idxmax() 方法选出每列中最大值的行索引标签：')
max_cols = college_n2.idxmax()
print(max_cols)

print('用 unique() 方法选出所有不重复的列名：')
unique_max_cols = max_cols.unique()
print(unique_max_cols[:5])

print('用max_cols选出只包含最大值的行，用style的 highlight_max() 高亮：')
print(college_n2.loc[unique_max_cols].style.highlight_max())

print('用axis参数可以高亮每行的最大值：')
college_n3 = pd.read_csv('../data/college.csv', index_col='INSTNM')
college_ugds = college_n3.filter(like='UGDS_').head()
print(college_ugds)
print(college_ugds.style.highlight_max(axis='columns'))



