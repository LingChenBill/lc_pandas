#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/7
# @Author: Lingchen
# @Prescription: 构建多个布尔条件
# 在 pandas中位运算符（&，|， ~）的优先级高于比较运算符。
import pandas as pd

movie = pd.read_csv('../data/movie.csv', index_col='movie_title')
print(movie.head())

print('构建多个布尔条件：')
criteria1 = movie.imdb_score > 8
criteria2 = movie.content_rating == 'PG-13'
criteria3 = (movie.title_year < 2000) | (movie.title_year >= 2010)
print('criteria2: ')
print(criteria2.head())

print('将多个布尔条件合并成一个：')
criteria_final = criteria1 & criteria2 & criteria3
print(criteria_final.head())
