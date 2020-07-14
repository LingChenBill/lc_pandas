#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/14
# @Author: Lingchen
# @Prescription: 用不等索引填充数值
#                % pip install jinja2
import pandas as pd
import numpy as np

print('读取数据集：')
baseball_14 = pd.read_csv('../data/baseball14.csv', index_col='playerID')
baseball_15 = pd.read_csv('../data/baseball15.csv', index_col='playerID')
baseball_16 = pd.read_csv('../data/baseball16.csv', index_col='playerID')
print(baseball_14.head())

print('用索引 difference 方法，找到哪些索引标签在 baseball_14 中，却不在 baseball_15 中: ')
print(baseball_14.index.difference(baseball_15.index))
print(baseball_14.index.difference(baseball_16.index))

print('找到每个球员在过去三上赛季中的击球数：H列包含了这个数据：')
hits_14 = baseball_14['H']
hits_15 = baseball_15['H']
hits_16 = baseball_16['H']
print(hits_14.head())

print('将两列相加：')
print((hits_14 + hits_15).head())

print('congeha01 和 corpoca01是有记录的，使用fill_value 来避免缺失值：')
print(hits_14.add(hits_15, fill_value=0).head())

print('再将2016年的数据也加上：')
hits_total = hits_14.add(hits_15, fill_value=0).add(hits_16, fill_value=0)
print(hits_total.head())

print('检查 hits_total 中是否有缺失值：')
print(hits_total.hasnans)

print('若一个元素中两个Series中都是缺失值，即使相加 且 使用了 fill_value，结果也仍然是缺失值：')
s = pd.Series(index=['a', 'b', 'c', 'd'], data=[np.nan, 3, np.nan, 1])
print('s: ')
print(s)

s1 = pd.Series(index=['a', 'b', 'c'], data=[np.nan, 6, 10])
print('s1: ')
print(s1)

print('s 和 s1 相加：')
print(s.add(s1, fill_value=5))
print('s1 和 s 相加：')
print(s1.add(s, fill_value=5))

print('从 baseball_14 选取一些列：')
df_14 = baseball_14[['G', 'AB', 'R', 'H']]
print(df_14.head())

print('从 baseball_15 中选取一些列：')
df_15 = baseball_15[['AB', 'R', 'H', 'HR']]
print(df_15.head())

print('将二者相加，只要行或列不能对齐，就会产生缺失值，高亮显示：')
# print((df_14 + df_15).head(10).style.highlight_null('yellow'))
print((df_14 + df_15).head(10))

print('即使使用add 中的fill_value, 也会有缺失值：')
# print(df_14.add(df_15, fill_value=0).head(10).style.highlight_null('yellow'))
print(df_14.add(df_15, fill_value=0).head(10))
