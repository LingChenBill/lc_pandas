#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/14
# @Author: Lingchen
# @Prescription: 在整个DataFrame上操作
import pandas as pd

pd.options.display.max_rows = 8
movie = pd.read_csv('data/movie.csv')
# 打印行数和列数
print(movie.shape)

# 打印数据的个数
print(movie.size)

# 该数据集的维度
print(movie.ndim)

# 该数据集的长度
print(len(movie))

# 各个列的值的个数
print(movie.count())

# 各列的最小值
print(movie.min())

# 打印描述信息
print(movie.describe())

# 使用percentiles参数指定分位数
pd.options.display.max_rows = 10
print(movie.describe(percentiles=[.01, .3, .99]))

# 打印各列空值的个数
pd.options.display.max_rows = 8
print(movie.isnull().sum())

# 设定skipna=False, 没有缺失值的数值列才会计算结果
print(movie.min(skipna=False))

