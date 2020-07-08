#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/7
# @Author: Lingchen
# @Prescription: 用布尔索引过滤
import pandas as pd

movie = pd.read_csv('data/movie.csv', index_col='movie_title')
print('创建第一个布尔条件：')
criteria1 = movie.imdb_score > 8
criteria2 = movie.content_rating == 'PG-13'
criteria3 = (movie.title_year < 2000) | (movie.title_year >= 2010)
final_criteria_a = criteria1 & criteria2 & criteria3

print('创建第二个布尔条件：')
criteria_b1 = movie.imdb_score < 5
criteria_b2 = movie.content_rating == 'R'
criteria_b3 = (movie.title_year >= 2000) | (movie.title_year <= 2010)
final_criteria_b = criteria_b1 & criteria_b2 & criteria_b3

print('将两个布尔条件用或运算符合并：')
final_criteria_all = final_criteria_a | final_criteria_b
print(final_criteria_all.head())

print('用最终的布尔条件过滤数据：')
print(movie[final_criteria_all].head())

print('使用loc指定特定的列，查看过滤条件是否起作用：')
cols = ['imdb_score', 'content_rating', 'title_year']
print(movie.loc[final_criteria_all, cols].head(10))

print('用一个长布尔表达式来代替前面的短表达式生成的布尔条件：')
criteria_a2 = (movie.imdb_score > 8) & \
              (movie.content_rating == 'PG-13') & \
              ((movie.title_year < 2000) | (movie.title_year > 2009))
print(criteria_a2.equals(final_criteria_a))
