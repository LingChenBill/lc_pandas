#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/12
# @Author: Lingchen
# @Prescription: 使用布尔值、整数、和标签进行选取
import pandas as pd
import numpy as np

movie = pd.read_csv('../data/movie.csv', index_col='movie_title')

print('根据布尔条件选取：')
c1 = movie['content_rating'] == 'G'
c2 = movie['imdb_score'] < 4
criteria = c1 & c2
movie_loc = movie.loc[criteria]
print(movie_loc.head())

print('检查loc条件与布尔条件创建出来的两个DataFrame是否一样：')
print(movie_loc.equals(movie[criteria]))

print('尝试使用iloc 来布尔索引，会出错：')
# movie_iloc = movie.iloc[criteria]

print('可以使用布尔值得到 ndarray, 用values可以取出array: ')
movie_iloc = movie.iloc[criteria.values]
print(movie_iloc.equals(movie_loc))
print(movie.loc[criteria.values])

print('布尔索引也可以来选取列：')
criteria_col = movie.dtypes == np.int64
print(criteria_col.head())
print(movie.loc[:, criteria_col].head())

print('因为 criteria_col 是包含行索引的一个Series, 必须要使用底层的 ndarray, 才能使用 iloc: ')
print(movie.iloc[:, criteria_col.values].head())

print('选取四列, 按照 imdb_score 列升序排列：')
cols = ['content_rating', 'imdb_score', 'title_year', 'gross']
print(movie.loc[criteria, cols].sort_values('imdb_score'))

print('用 get_loc 获取这四列的整数位置：')
col_index = [movie.columns.get_loc(col) for col in cols]
print(col_index)

print('用 iloc 来选取数据：')
print(movie.iloc[criteria.values, col_index].sort_values('imdb_score'))

print('查看Series的底层结构：')
a = criteria.values
print(a[:5])

print(len(a), len(criteria))

print('传入的布尔索引可以跟DataFrame的长度不同：')
# print(movie.loc[[True, False, True, False], [True, False, False, True]])
