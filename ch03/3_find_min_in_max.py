#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/27
# @Author: Lingchen
# @Prescription: 在最大中选择最小
import pandas as pd

movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'imdb_score', 'budget']]
print(movie2.head())

print('选取imdb_score分数最高的100个: ')
print(movie2.nlargest(100, 'imdb_score').head())

print('用链式操作，再从最大中挑出预算最小的5个：')
print(movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget').head())
