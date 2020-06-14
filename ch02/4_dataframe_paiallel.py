#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/14
# @Author: Lingchen
# @Prescription: 串联DataFrame方法
import pandas as pd

movie = pd.read_csv('data/movie.csv')

# 使用isnull()将每个值转变为布尔值
print(movie.isnull().head())

# 使用sum统计布尔值，返回的是Series
print(movie.isnull().sum().head())

# 对这个Series再使用sum, 返回整个DataFrame的缺失值的个数，返回值是个标题
print(movie.isnull().sum().sum())

# 判断整个DataFrame有没有缺失值，方法是连着使用两个any
print(movie.isnull().any().any())

# isnull返回同样大小的DataFrame，但所有的值变为布尔值
# AttributeError: 'DataFrame' object has no attribute 'get_dtype_counts'
# print(movie.isnull().get_dtype_counts)

# movie数据集的对象数据包含缺失值。默认条件下，聚合方法min, max, sum不会返回任何值
print(movie[['color', 'movie_title', 'color']].max())

# 要让pandas强行每行返回每列的值，必须填入缺失值
print(movie.select_dtypes(['object']).fillna('').max())



