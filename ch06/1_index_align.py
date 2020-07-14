#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/13
# @Author: Lingchen
# @Prescription: 检查索引
import pandas as pd

college = pd.read_csv('../data/college.csv')

print('读取 college 数据集，提取所有列：')
columns = college.columns
print(columns)

print('访问底层的数组：')
print(columns.values)

print('取出该数组的第6个数：')
print(columns[5])

print('取出该数组的第2、9、11的值：')
print(columns[[1, 8, 10]])

print('逆序切取：')
print(columns[-7:-4])

print('索引有许多与 DataFrame 相同的方法：')
print(columns.min(), columns.max(), columns.isnull().sum())

print('索引对象可以通过字符串修改：')
print(columns + '_A')

print('索引对象也可以通过比较运算符，得到布尔索引：')
print(columns > 'G')

print('尝试修改索引，会出错，索引不可修改：')
# columns[1] = 'city'

print('索引支持集合运算：联合，交叉，求差，对称差：')
print('切片：')
c1 = columns[:4]
print(c1)

c2 = columns[2:5]
print(c2)

print('联合：')
print(c1.union(c2))
print(c1 | c2)

print('对称差：')
print(c1.symmetric_difference(c2))
print(c1 ^ c2)
