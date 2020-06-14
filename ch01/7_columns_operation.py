#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/13
# @Author: Lingchen
# @Prescription: 创建、删除列
import pandas as pd

movie = pd.read_csv('data/movie.csv')
movie['has_seen'] = 0
print(movie.columns)

# 给新列赋值
movie['actor_director_facebook_likes'] = (
    movie['actor_1_facebook_likes'] +
    movie['actor_2_facebook_likes'] +
    movie['actor_3_facebook_likes'] +
    movie['director_facebook_likes']
)
print(movie['actor_director_facebook_likes'])
print(movie['actor_director_facebook_likes'].isnull().sum())

# 用all()检查是否所有的布尔值都为True
movie['actor_director_facebook_likes'] = movie['actor_director_facebook_likes'].fillna(0)
movie['is_cast_likes_more'] = (
    movie['cast_total_facebook_likes'] >= movie['actor_director_facebook_likes']
)
print(movie['is_cast_likes_more'].all())

# 删除列
movie = movie.drop('actor_director_facebook_likes', axis='columns')
movie['actor_total_facebook_likes'] = (
        movie['actor_1_facebook_likes'] +
        movie['actor_2_facebook_likes'] +
        movie['actor_3_facebook_likes']
)
movie['actor_total_facebook_likes'] = movie['actor_total_facebook_likes'].fillna(0)

movie['is_cast_likes_more'] = (
        movie['cast_total_facebook_likes'] >= movie['actor_total_facebook_likes']
)

print(movie['is_cast_likes_more'].all())

# 创建新列
movie['pct_actor_cast_like'] = (
    movie['actor_total_facebook_likes'] / movie['cast_total_facebook_likes']
)

print(movie['pct_actor_cast_like'].min(), movie['pct_actor_cast_like'].max())
# 查看特定的列
print(movie.set_index('movie_title')['pct_actor_cast_like'].head())

# 用insert()方法原地插入列
# 获取列索引
profit_index = movie.columns.get_loc('gross') + 1
print(profit_index)

movie.insert(loc=profit_index,
             column='profit',
             value=movie['gross'] - movie['budget'])
print(movie.head())
print(movie['profit'].head())
# print(movie)
