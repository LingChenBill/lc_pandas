#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/12
# @Author: Lingchen
# @Prescription: 用 where 方法保留Series
import pandas as pd
import matplotlib.pyplot as plt

print('读取movie数据集：')
movie = pd.read_csv('../data/movie.csv', index_col='movie_title')
print('actor_1_facebook_likes 列删除缺失省：')
fb_likes = movie['actor_1_facebook_likes'].dropna()
print(fb_likes.head())

print('使用 describes 获取对数据的认知：')
print(fb_likes.describe(percentiles=[.1, .25, .5, .75, .9]).astype(int))
# print(fb_likes.describe(percentiles=[.1, .25, .5, .75, .9]))

print('画一张柱状图：')
# fb_likes.hist()
# plt.show()

print('检测小于20000个喜欢的比例：')
criteria_high = fb_likes < 20000
print(criteria_high.mean().round(2))

print('where 可以返回一个同样大小的Series, 但是所有False会被替换成缺失值：')
print(fb_likes.where(criteria_high).head())

print('where 第二个参数可以让你替换缺失值：')
print(fb_likes.where(criteria_high, other=20000).head())

print('通过where条件，可以设定上下限的值：')
criteria_low = fb_likes > 300
fb_likes_cap = fb_likes.where(criteria_high, other=20000) \
                       .where(criteria_low, 300)

print(fb_likes_cap.head())

print('原始的Series 和 新修改过的Series 的长度是一样的：')
print(len(fb_likes), len(fb_likes_cap))
fb_likes_cap.hist()
plt.show()

fb_likes_clips = fb_likes.clip(lower=300, upper=20000)
print(fb_likes_cap.equals(fb_likes_clips))
