#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/12
# @Author: Lingchen
# @Prescription: 对 DataFrame 的行进行 Mask
import pandas as pd
from pandas.testing import assert_frame_equal
import time

movie = pd.read_csv('../data/movie.csv', index_col='movie_title')
criteria_1 = movie['title_year'] >= 2010
criteria_2 = movie['title_year'].isnull()
criteria = criteria_1 | criteria_2

print('使用 mask 使所有满足条件的数据消失：')
print(movie.mask(criteria).head())

print('去除缺失值：')
movie_mask = movie.mask(criteria).dropna(how='all')
print(movie_mask.head())

print('用布尔索引选取电影 title_year 小于2010的电影：')
movie_bool = movie[movie['title_year'] < 2010]
print(movie_bool.head())

print('判断两者是否相同：')
print(movie_mask.equals(movie_bool))

print('判断两者的形状是否相同：')
print(movie_mask.shape == movie_bool.shape)

print('判断两者的数据类型是否相同：')
print('mask 方法产生了许多的缺失值，缺失值默认是float值类型，之前的整数型转换成float类型：')
print(movie_mask.dtypes == movie_bool.dtypes)

print('assert_frame_equal 可以判断两个Pandas对象是否相同，而不检测数据类型：')
print(assert_frame_equal(movie_bool, movie_mask, check_dtype=False))

print('测试两者的速度：')
start = time.perf_counter()
movie.mask(criteria).dropna(how='all')
stop = time.perf_counter()
print('Time1: ', stop - start)

start = time.perf_counter()
movie[movie['title_year'] < 2010]
stop = time.perf_counter()
print('Time2: ', stop - start)












