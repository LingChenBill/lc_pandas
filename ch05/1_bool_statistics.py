#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/5
# @Author: Lingchen
# @Prescription: 计算布尔值统计信息
import pandas as pd

print('读取movie，设定行索引：')
pd.options.display.max_columns = 6
movie = pd.read_csv('data/movie.csv', index_col='movie_title')
print(movie.head())

print('判断电影时长是否超过2个小时：')
movie_2_hours = movie['duration'] > 120
print(movie_2_hours.head(10))

print('有多少时长超过2小时的电影：')
print(movie_2_hours.sum())

print('超过2小时电影的比例：')
print(movie_2_hours.mean())

print('用 describe 输出一些该布尔Series信息：')
print(movie_2_hours.describe())

print('实际上duration这一列有缺省值的，获取真正的超过2小时的电影：')
print(movie['duration'].dropna().gt(120).mean())

print('统计False和True值的比例：')
print(movie_2_hours.value_counts(normalize=True))

print('比较同一个DataFrame的两列：')
actors = movie[['actor_1_facebook_likes', 'actor_2_facebook_likes']].dropna()
print((actors['actor_1_facebook_likes'] > actors['actor_2_facebook_likes']).mean())



