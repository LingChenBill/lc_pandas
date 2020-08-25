#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/8/25
# @Author: Lingchen
# @Prescription: 用 apply 计算每州的加权平均SAT分数
import pandas as pd
import numpy as np
from collections import OrderedDict
from scipy.stats import gmean, hmean

print('读取 college, UGDS, SATMTMID, SATVRMID 三列如果有缺失则删除行：')
college = pd.read_csv('../data/college.csv')
subset = ['UGDS', 'SATMTMID', 'SATVRMID']
college2 = college.dropna(subset=subset)
print(college.shape)
print(college2.shape)

print('自定义一个求SAT 数学成绩的加权平均值的函数: ')


def weighted_math_average(df):
    """
    自定义一个求SAT 数学成绩的加权平均值的函数
    :param df:
    :return:
    """
    weighted_math = df['UGDS'] * df['SATMTMID']
    return int(weighted_math.sum() / df['UGDS'].sum())


print('按州分组，并调用apply方法，传入自定义函数：')
print(college2.groupby('STABBR').apply(weighted_math_average).head())

print('效果同上：')
# print(college2.groupby('STABBR').agg(weighted_math_average).head())

print('如果将列限制到SATMTMID,会报错，这是因为不能访问UGDS：')
print("KeyError: 'UGDS'")
# print(college2.groupby('STABBR')['SATMTMID'].agg(weighted_math_average))

print('apply的一个不错的功能是通过返回Series, 创建多个新的列: ')


def weighted_average(df):
    """
    apply的一个不错的功能是通过返回Series, 创建多个新的列
    :param df:
    :return:
    """
    data = OrderedDict()
    weight_m = df['UGDS'] * df['SATMTMID']
    weight_v = df['UGDS'] * df['SATVRMID']

    data['weighted_math_avg'] = weight_m.sum() / df['UGDS'].sum()
    data['weighted_verbal_avg'] = weight_v.sum() / df['UGDS'].sum()
    data['math_avg'] = df['SATMTMID'].mean()
    data['verbal_avg'] = df['SATVRMID'].mean()
    data['count'] = len(df)
    return pd.Series(data, dtype='float')


print(college2.groupby('STABBR').apply(weighted_average).head(10))


def calculate_means(df):
    """
    自定义一个返回DataFrame函数，使用Numpy的函数average计算加权平均值，使用Scipy的gmean和hmean计算几何和调和平均值
    :param df:
    :return:
    """
    df_means = pd.DataFrame(index=['Arithmetic', 'Weighted', 'Geometric', 'Harmonic'])
    cols = ['SATMTMID', 'SATVRMID']
    for col in cols:
        arithmetic = df[col].mean()
        weighted = np.average(df[col], weights=df['UGDS'])
        geometric = gmean(df[col])
        harmonic = hmean(df[col])
        df_means[col] = [arithmetic, weighted, geometric, harmonic]

    df_means['count'] = len(df)
    return df_means.astype(int)


print('自定义一个返回DataFrame函数，使用Numpy的函数average计算加权平均值，使用Scipy的gmean和hmean计算几何和调和平均值: ')
print(college2.groupby('STABBR').filter(lambda x: len(x) != 1).groupby('STABBR').apply(calculate_means).head(10))

