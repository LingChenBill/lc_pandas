#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/27
# @Author: Lingchen
# @Prescription: 通过排序选取每组中的最大值
import pandas as pd

movie = pd.read_csv('../data/movie.csv')
movie2 = movie[['movie_title', 'title_year', 'imdb_score']]
print('movie2按照title_year降序排列: ')
print(movie2.sort_values('title_year', ascending=False).head())

print('用列表同时对两列进行排序: ')
print(movie2.sort_values(['title_year', 'imdb_score'], ascending=False).head())

print('运用drop_duplicates去重，只保留每一年的第一条数据：')
movie3 = movie2.sort_values(['title_year', 'imdb_score'], ascending=False)
print(movie3.drop_duplicates(subset='title_year').head())

print('可以对ascending设置列表，可以同时一列降序排列，一列升序排列：')
movie4 = movie[['movie_title', 'title_year', 'content_rating', 'budget']]
movie4_sorted = movie4.sort_values(['title_year', 'content_rating', 'budget'],
                                   ascending=[False, False, True])
print(movie4_sorted.drop_duplicates(subset=['title_year', 'content_rating']).head(10))
