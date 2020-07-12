#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/27
# @Author: Lingchen
# @Prescription: 用整数和标签来选取数据
import pandas as pd

print('用索引方法get_loc，找到指定列的整数位置：')
college = pd.read_csv('../data/college.csv', index_col='INSTNM')
col_start = college.columns.get_loc('UGDS_WHITE')
col_stop = college.columns.get_loc('UGDS_UNKN') + 1
print((col_start, col_stop))

print('用切片选取连续的列：')
print(college.iloc[:5, col_start:col_stop])

print('index可以获取整数行的标签名：')
row_start = college.index[10]
row_stop = college.index[15]
print(college.loc[row_start:row_stop, 'UGDS_WHITE':'UGDS_UNKN'])


