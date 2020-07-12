#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/5
# @Author: Lingchen
# @Prescription: 惰性行切片
# 惰性切片不能用于列，只能用于DataFrame和Series，也不能同时选取行和列
import pandas as pd

print('从行索引10到20，每隔一个取一行：')
college = pd.read_csv('../data/college.csv', index_col='INSTNM')
print(college[10:20:2])

print('Series也可以同样切片：')
city = college['CITY']
print(city[10:20:2])

print('查看行4002行标签：')
print(college.index[4001])

print('Series和DataFrame都可以用标签进行切片，DataFrame切片：')
start = 'Mesa Community College'
stop = 'Spokane Community College'
print(college[start:stop:1500])

print('对Series进行切片：')
print(city[start:stop:1500])

# print('尝试选取两列，导致错误：')
# print(college[:10, ['CITY', 'STABBR']])

print('用loc和iloc来选取：')
first_ten_instnm = college.index[:10]
print(college.loc[first_ten_instnm, ['CITY', 'STABBR']])

