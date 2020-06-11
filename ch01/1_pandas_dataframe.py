#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/11
# @Author: Lingchen
# @Prescription:
import pandas as pd

# 设置最大列数和最大行数
pd.set_option('max_columns', 8, 'max_rows', 10)

# 用read_csv()方法读取csv文件
# head()方法可以默认读取文件前5行，head(n)读取前n行
movie = pd.read_csv('data/movie.csv')
# print(movie.head())
# print(movie.head(2))

# 提取列索引
columns = movie.columns
print(columns)

# 提取行索引
index = movie.index
print(index)

# 提取数据
data = movie.values
print(data)

# index的类型
print(type(index))

# columns的类型
print(type(columns))

# data类型
print(type(data))

# 判断是不是子类型
print(issubclass(pd.RangeIndex, pd.Index))

# 访问index的值, index是一个列表，可以切片或索引
print(index.values)
print(index.values[0])

# 访问columns的值
print(columns.values)

# 各列的数据类型
print(movie.dtypes)

# 显示各类型的数量
# AttributeError: 'DataFrame' object has no attribute 'get_dtype_counts'
# print(movie.get_dtype_counts())

