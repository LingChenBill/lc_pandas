#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/8/20
# @Author: Lingchen
# @Prescription: 定义聚合(page_161)
import pandas as pd
import numpy as np

print('读取flights数据集，查询头部：')
flights = pd.read_csv('../data/flights.csv')
print(flights.head())

print('按照 AIRLINE 分组，使用 agg 方法，传入要聚合的列和聚合函数：')
print(flights.groupby('AIRLINE').agg({'ARR_DELAY': 'mean'}).head())

print('选取列使用索引，聚合函数作为字符串传入agg：')
print(flights.groupby('AIRLINE')['ARR_DELAY'].agg('mean').head())

print('也可以向agg中传入NumPy的mean函数：')
print(flights.groupby('AIRLINE')['ARR_DELAY'].agg(np.mean).head())

print('也可以直接使用mean()函数：')
print(flights.groupby('AIRLINE')['ARR_DELAY'].mean().head())

print('groupby方法产生的是一个DataFrameGroupBy对象：')
grouped = flights.groupby('AIRLINE')
print(type(grouped))

print('如果agg接收到的不是聚合函数，则会导致异常：')
print('ValueError: Function does not reduce')
# print(flights.groupby('AIRLINE')['ARR_DELAY'].agg(np.sqrt))
