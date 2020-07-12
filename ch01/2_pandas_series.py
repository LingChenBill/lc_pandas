#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/11
# @Author: Lingchen
# @Prescription:
import pandas as pd

movie = pd.read_csv('../data/movie.csv')
# 选择director_name这列
print(movie['director_name'])

# 通过属性的方式获取
print(movie.director_name)

# 查看类型，Series
print(type(movie['director_name']))

# 查看选取列的名字
director = movie['director_name']
print(director.name)

# 单列的Series转换成DataFrame
print(director.to_frame().head())


