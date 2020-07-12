#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/8
# @Author: Lingchen
# @Prescription: 用标签索引替代布尔索引
import pandas as pd
import time

college = pd.read_csv('../data/college.csv')
print('用布尔索引选取所有的得克萨斯达的学校：')
print(college[college['STABBR'] == 'TX'].head())

print('用 STABBR作为行索引，然后用loc进行索引： ')
college2 = college.set_index('STABBR')
print(college2.loc['TX'].head())

print('比较两者的速度：')
start = time.perf_counter()
college[college['STABBR'] == 'TX']
stop = time.perf_counter()
print('time1: ', stop - start)

start = time.perf_counter()
college2 = college.set_index('STABBR')
college2.loc['TX']
stop = time.perf_counter()
print('time2: ', stop - start)

print('使用布尔索引和标签选取多列：')
states = ['TX', 'CA', 'NY']
print(college[college['STABBR'].isin(states)].head())
print(college2.loc[states].head())
