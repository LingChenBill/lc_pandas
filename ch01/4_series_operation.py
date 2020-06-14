#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/13
# @Author: Lingchen
# @Prescription:
import pandas as pd

pd.set_option('max_rows', 8)
movie = pd.read_csv('data/movie.csv')
imdb_score = movie['imdb_score']
print(imdb_score)

# 每列值 + 1
print(imdb_score + 1)

# 每列值 * 2.5
print(imdb_score * 2.5)

# 每列值除以7的余数
print(imdb_score // 7)

# 判断是否大于7
print(imdb_score > 7)

# 判断是否等于字符串
director = movie['director_name']
print(director == 'James Cameron')

# 利用通用函数实现加法
print(imdb_score.add(1))

# 利用通用函数实现乘法
print(imdb_score.mul(2.5))

# 利用通用函数实现底除
print(imdb_score.floordiv(7))

# 利用通用函数实现大于7
print(imdb_score.gt(7))

# 利用通用函数实现等于
print(director.eq('James Cameron'))

# 利用通用函数实现取模
print(imdb_score.astype(int).mod(5))

a = type(imdb_score)
print(a)
print(a([1, 2, 3]))

