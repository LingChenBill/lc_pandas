#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/5
# @Author: Lingchen
# @Prescription: 按字母切片
# 先排序再字母切片
import pandas as pd

college = pd.read_csv('data/college.csv', index_col='INSTNM')
# print(college.loc['Sp':'Su'])

print('对college进行排序：')
college = college.sort_index()
print(college.head())

print('再进行尝试选取字母顺序在 Sp 和 Su 之间的学校：')
pd.options.display.max_rows = 6
print(college.loc['Sp':'Su'])

print('可以用 is_monotonic_decreasing 和 来检测字母排序的顺序：')
college = college.sort_index(ascending=False)
# print(college.index.is_monotonic_decreasing)
print(college.index.is_monotonic_increasing)

print('字母逆序选取：')
print(college.loc['E':'B'])

