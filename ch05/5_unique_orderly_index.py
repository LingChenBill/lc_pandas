#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/8
# @Author: Lingchen
# @Prescription: 用唯一和有序索引选取
import pandas as pd
import time

print('检查 STABBR 行索引是否有序：')
college = pd.read_csv('../data/college.csv')
college2 = college.set_index('STABBR')
print(college2.index.is_monotonic)

print('将college2排序，存储为另一个对象，再判断行索引是否有序：')
college3 = college2.sort_index()
print(college3.index.is_monotonic)

print('从这三个DataFrame中，比较速度：')
start = time.perf_counter()
college[college['STABBR'] == 'TX']
stop = time.perf_counter()
print('Time1: ', stop - start)

start = time.perf_counter()
college2.loc['TX']
stop = time.perf_counter()
print('Time2: ', stop - start)

start = time.perf_counter()
college3.loc['TX']
stop = time.perf_counter()
print('Time3: ', stop - start)
print('有序条件下的loc选取速度最快！')

print('将INSTNM 作为行索引，判断行索引是否有序：')
college_unique = college.set_index('INSTNM')
print(college_unique.index.is_unique)

print('使用布尔条件选取：')
# print(college_unique[college_unique['INSTNM'] == 'Stanford University'])
start = time.perf_counter()
print(college[college['INSTNM'] == 'Stanford University'])
stop = time.perf_counter()
print('Time4: ', stop - start)

print('用行索引标签选取：')
start = time.perf_counter()
print(college_unique.loc['Stanford University'])
stop = time.perf_counter()
print('Time5: ', stop - start)

print('使用 CITY 和 STABBR 两列作为行索引，并排序：')
college.index = college['CITY'] + ', ' + college['STABBR']
college.sort_index()
print(college.head())

print('选取 Miami, FL的大学：')
print(college.loc['Miami, FL'].head())

print('比较速度：')
start = time.perf_counter()
crit_1 = college['CITY'] == 'Miami'
crit_2 = college['STABBR'] == 'FL'
print(college[crit_1 & crit_2])
stop = time.perf_counter()
print('Time6: ', stop - start)

start = time.perf_counter()
print(college.loc['Miami, FL'])
stop = time.perf_counter()
print('Time7: ', stop - start)

print('判断这两个条件是否相等：')
print(college[crit_1 & crit_2].equals(college.loc['Miami, FL']))
