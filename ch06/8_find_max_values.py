#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/8/19
# @Author: Lingchen
# @Prescription: 找到最常见的最大值（page_159）
import pandas as pd

print('读取college, 过滤出只包含本科生种族的比例信息的列：')
pd.options.display.max_rows = 40
college = pd.read_csv('../data/college.csv', index_col='INSTNM')
college_ugds = college.filter(like='UGDS_')
print(college_ugds.head())

print('用idxmax 方法选出每行种族比例最高的列名：')
highest_percentage_race = college_ugds.idxmax(axis='columns')
print(highest_percentage_race.head())

print('用 value_counts 查看最大值的分布：')
print(highest_percentage_race.value_counts(normalize=True))

print('对于黑人比例最高的学校，排名第二的种族的分布情况：')
college_black = college_ugds[highest_percentage_race == 'UGDS_BLACK']
college_black = college_black.drop('UGDS_BLACK', axis='columns')
print(college_black.idxmax(axis='columns').value_counts(normalize=True))

