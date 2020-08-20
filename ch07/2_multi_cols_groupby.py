#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/8/20
# @Author: Lingchen
# @Prescription: 用多个列和函数进行分组和聚合
import pandas as pd

flights = pd.read_csv('../data/flights.csv')
print(flights.head())

print('每家航空公司每周平均每天取消的航班数：')
print(flights.groupby(['AIRLINE', 'WEEKDAY'])['CANCELLED'].agg('sum').head(7))

print('分组可以是多组，选取可以是多组，聚合函数也可以是多个')
print('每周每家航空公司取消或改变航线的航班总数和比例：')
print(flights.groupby(['AIRLINE', 'WEEKDAY'])['CANCELLED', 'DIVERTED'].agg(['sum', 'mean']).head(7))

print('用列表和嵌套字典对多列分组和聚合：')
print('对于每条航线，找到总航总数，取消的数量和比例，飞行时间的平均时间和方差：')
group_cols = ['ORG_AIR', 'DEST_AIR']
agg_dict = {'CANCELLED': ['sum', 'mean', 'size'],
            'AIR_TIME': ['mean', 'var']}
print(flights.groupby(group_cols).agg(agg_dict).head())
