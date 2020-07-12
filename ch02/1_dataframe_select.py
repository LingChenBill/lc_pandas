#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/14
# @Author: Lingchen
# @Prescription: 选取多个DataFrame列
import pandas as pd

movie = pd.read_csv('../data/movie.csv')

# 用列表选取多个列
movie_actor_director = movie[['actor_1_name', 'actor_2_name',
                              'actor_3_name', 'director_name']]
print(movie_actor_director.head())

# 选取单列(带标题)
# print(movie['director_name'].head())
print(movie[['director_name']].head())

# 错误的选取多列的方式,方括号
# KeyError: ('actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name')
# print(movie['actor_1_name', 'actor_2_name',
#             'actor_3_name', 'director_name'].head())

# 将列表赋值给一个变量，便于多选
cols = ['actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name']
movie_actor_director = movie[cols]
print(movie_actor_director)

# 选取整数列
print(movie.select_dtypes(include=['int', 'float64']).head())
# print(movie['num_critic_for_reviews'].dtype)

# 选取所有的数值列
print(movie.select_dtypes(include=['number']).head())

# 通过filter()函数过滤器选取多列
print(movie.filter(like='facebook').head())

# 通过正则表达式选取多列
print(movie.filter(regex='\d').head())

# 通过filter()函数，传递列表参数到items，选取多列
print(movie.filter(items=['actor_1_name', 'asdf']).head())
