#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/13
# @Author: Lingchen
# @Prescription: 使用索引
import pandas as pd

movie = pd.read_csv('../data/movie.csv')
print(movie.shape)

# set_index()给行索引命名
movie2 = movie.set_index('movie_title')
print(movie2)

# 通过index_col参数命名
movie3 = pd.read_csv('../data/movie.csv', index_col='movie_title')
print(movie3)

# 复原索引
print(movie3.reset_index())

# 通过rename()重命名
idx_name = {'Avatar': 'Ratava', 'Spectre': 'Ertceps'}
col_name = {'director_name': 'Director Name',
            'num_critic_for_reviews': 'Critical Reviews'}
print(movie3.rename(index=idx_name, columns=col_name).head())

index = movie2.index
columns = movie2.columns

index_list = index.tolist()
column_list = columns.tolist()
print(index_list[:5])
print(column_list)

index_list[0] = 'Ratava'
index_list[2] = 'Ertceps'
column_list[1] = 'Director Name'
column_list[2] = 'Critical Reviews'
print(index_list)
print(column_list)


