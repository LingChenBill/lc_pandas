#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/8/22
# @Author: Lingchen
# @Prescription: 自定义聚合函数（page_172）
import pandas as pd

college = pd.read_csv('../data/college.csv')
print(college.head())

print('求出每个州的本科生的平均值和标准差：')
# print(college.columns)
print(college.groupby('STABBR')['UGDS'].agg(['mean', 'std']).round(0).head())


def max_deviation(s):
    """
    远离平均值的标准差的最大个数，写一个自定义函数
    :param s:
    :return:
    """
    std_score = (s - s.mean()) / s.std()
    return std_score.abs().max()


print('agg聚合函数在调用方法时，直接引入自定义的函数名：')
print(college.groupby('STABBR')['UGDS'].agg(max_deviation).round(1).head())

print('自定义的聚合函数也适用于多个数值列：')
print(college.groupby('STABBR')['UGDS', 'SATVRMID', 'SATMTMID'].agg(max_deviation).round(1).head())

print('自定义聚合函数也可以和预先定义的函数一起使用：')
print(college.groupby(['STABBR', 'RELAFFIL'])['UGDS', 'SATVRMID', 'SATMTMID']
      .agg([max_deviation, 'mean', 'std']).round(1).head())

print('自定义函数名：')
print(max_deviation.__name__)
print('修改函数名：')
max_deviation.__name__ = 'Max Deviation'
print(college.groupby(['STABBR', 'RELAFFIL'])['UGDS', 'SATVRMID', 'SATMTMID']
      .agg([max_deviation, 'mean', 'std']).round(1).head())
