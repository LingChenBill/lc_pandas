#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/13
# @Author: Lingchen
# @Prescription: 串联Series方法
import pandas as pd

movie = pd.read_csv('data/movie.csv')
actor_1_fb_likes = movie['actor_1_facebook_likes']
director = movie['director_name']

# 计数，查看前三
print(director.value_counts().head(3))

# 统计缺失值的数量
print(actor_1_fb_likes.isnull().sum())

# 查看列的数据类型
print(actor_1_fb_likes.dtype)
print(director.dtype)

# 缺失值填充为0，转换为整形，查看前5
print(actor_1_fb_likes.fillna(0)
      .astype(int)
      .head())

# 缺失值的比例
print(actor_1_fb_likes.isnull().mean())
