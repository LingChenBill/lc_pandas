#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/27
# @Author: Lingchen
# @Prescription: 用sorted_values来模拟nlargest
import pandas as pd

movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'imdb_score', 'budget']]
print('查找100个最大列中，预算列最小的5列：')
movie_smallest_largest = movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget')
print(movie_smallest_largest)

print('使用sort_values来选取imdb_score最高的100个：')
print(movie2.sort_values('imdb_score', ascending=False).head(100).sort_values('budget', ascending=True).head())

print('使用tail进行调查：')
print(movie2.nlargest(100, 'imdb_score').tail())
print('去掉head，重新：')
print(movie2.sort_values('imdb_score', ascending=False).head(100).sort_values('budget', ascending=True).head())
# print(movie2.sort_values('imdb_score', ascending=False).head(100).tail())
