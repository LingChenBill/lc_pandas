#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/8/20
# @Author: Lingchen
# @Prescription: 分组后去除多级索引（page_168）
import pandas as pd

print('读取数据：')
flights = pd.read_csv('../data/flights.csv')
print(flights.head())

print('按 AIRLINE , WEEKDAY分组，分别对 DIST 和 ARR_DELAY 聚合：')
airline_info = flights.groupby(['AIRLINE', 'WEEKDAY']).agg({'DIST': ['sum', 'mean'],
                                                            'ARR_DELAY': ['min', 'max']}).astype(int)
print(airline_info.head())

print('行和列都有两级索引，get_level_values(0) 取出第一级索引：')
level0 = airline_info.columns.get_level_values(0)
print(level0)

print('get_level_values(1)取出第二级索引：')
level1 = airline_info.columns.get_level_values(1)
print(level1)

print('一级和二级索引拼接成新的列索引：')
airline_info.columns = level0 + '_' + level1
print(airline_info.head(7))

print(' reset_index() 可以将行索引变成单级：')
print(airline_info.reset_index().head(7))

print('Pandas默认会在分组运算后，将所有分组的列放在索引中，as_index设为False可以避免这么做。')
print('分组后可以使用reset_index, 也可以达到同样的效果：')
print(flights.groupby(['AIRLINE'], as_index=False)['DIST'].agg('mean').round(0))

print('上面这么做，会默认对AIRLINE排序，sort 设为False可以避免排序：')
print(flights.groupby(['AIRLINE'], as_index=False, sort=False)['DIST'].agg('mean'))

