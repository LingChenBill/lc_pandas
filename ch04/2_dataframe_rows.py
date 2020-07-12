#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/27
# @Author: Lingchen
# @Prescription: 选取DataFrame的行
import pandas as pd

print('读取college的数据集：')
college = pd.read_csv('../data/college.csv', index_col='INSTNM')
print(college.head())

print('选取第61行：')
pd.options.display.max_rows = 6
print(college.iloc[60])

print('可以通过行标签选取：')
print(college.loc['University of Alaska Anchorage'])

print('选取多个不连续的行：')
print(college.iloc[[60, 99, 3]])

print('通过locl加列表来选取：')
labels = ['University of Alaska Anchorage',
          'International Academy of Hair Design',
          'University of Alabama in Huntsville']
print(college.loc[labels])

print('iloc可以用切片来连续选取：')
print(college.iloc[99:102])

print('loc可以用标签连接选取：')
start = 'International Academy of Hair Design'
stop = 'Mesa Community College'
print(college.loc[start:stop])

print('提取索引标签，生成一个列表')
print(college.iloc[[60, 99, 3]].index.tolist())
