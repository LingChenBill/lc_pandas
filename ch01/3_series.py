#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/12
# @Author: Lingchen
# @Prescription:
import pandas as pd

# 查看series所有不重复的指令
s_attr_methods = set(dir(pd.Series))
# 该集合的大小
print(len(s_attr_methods))

# 查看DataFrame所有不重复的指令
df_attr_methods = set(dir(pd.DataFrame))
print(len(df_attr_methods))

print(len(s_attr_methods & df_attr_methods))

# 选取director_name 和 actor_1_facebook_likes 两列
movie = pd.read_csv('data/movie.csv')
director = movie['director_name']
actor_1_facebook_likes = movie['actor_1_facebook_likes']
print(director.head())
print(actor_1_facebook_likes.head())

# 分别计数, max_rows显示的最大行数
pd.set_option('max_rows', 10)
print(director.value_counts())
print(actor_1_facebook_likes.value_counts())

print(director.size)
print(director.shape)
print(len(director))

# 有多个非空值
print(director.count())

print(actor_1_facebook_likes.size)
print(actor_1_facebook_likes.count())

# 显示actor_1_facebook_likes的中位分位数
print(actor_1_facebook_likes.quantile())

# 最小值
print(actor_1_facebook_likes.min())
# 最大值
print(actor_1_facebook_likes.max())
# 平均值
print(actor_1_facebook_likes.mean())
# 中位数
print(actor_1_facebook_likes.median())
# 标准差
print(actor_1_facebook_likes.std())
# 总和
print(actor_1_facebook_likes.sum())

# 打印描述信息
print(actor_1_facebook_likes.describe())
print(director.describe())
print(actor_1_facebook_likes.quantile(.2))

# 各个十分之一分位数
print(actor_1_facebook_likes.quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9]))

# 非空值
print(director.isnull())

# 填充缺失值
actor_1_facebook_likes_filled = actor_1_facebook_likes.fillna(0)
print(actor_1_facebook_likes_filled.count())

# 删除缺失值
actor_1_facebook_likes_dropped = actor_1_facebook_likes.dropna()
print(actor_1_facebook_likes_dropped.size)

# 返回频率
print(director.value_counts(normalize=True))

# 判断是否含有缺失值
print(director.hasnans)

# 判断是否是非缺失值
print(director.notnull())



