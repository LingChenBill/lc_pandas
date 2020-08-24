#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/8/23
# @Author: Lingchen
# @Prescription: 过滤状态（page_184）
import pandas as pd

college = pd.read_csv('../data/college.csv', index_col='INSTNM')
grouped = college.groupby('STABBR')
print(grouped.ngroups)

print('这等于求出不同州的个数，nunique() 可以得到同样的结果：')
print(college['STABBR'].nunique())

print('自定义一个计算少数民族学生总比例的函数，如果比例大于阈值，还返回True: ')


def check_minority(df, threshold):
    """
    自定义一个计算少数民族学生总比例的函数，如果比例大于阈值，还返回True
    :param df:
    :param threshold:
    :return:
    """
    minority_pct = 1 - df['UGDS_WHITE']
    total_minority = (df['UGDS'] * minority_pct).sum()
    total_ugds = df['UGDS'].sum()
    total_minority_pct = total_minority / total_ugds
    return total_minority_pct > threshold


print('grouped 变量有一个filter方法，可以接收一个自定义函数，决定是否保留一个分组：')
college_filtered = grouped.filter(check_minority, threshold=.5)
print(college_filtered.head())

print('通过查看形状，可以看到过滤了60%，只有20%个州的少数学生占据多数：')
print(college.shape)
print(college_filtered.shape)
print(college_filtered['STABBR'].nunique())

print('用一些不同的阈值，检查形状和不同州的个数：')
college_filtered_20 = grouped.filter(check_minority, threshold=.2)
print(college_filtered_20.shape)
print(college_filtered_20['STABBR'].nunique())

college_filtered_70 = grouped.filter(check_minority, threshold=.7)
print(college_filtered_70.shape)
print(college_filtered_70['STABBR'].nunique())

college_filtered_95 = grouped.filter(check_minority, threshold=.95)
print(college_filtered_95.shape)
print(college_filtered_95['STABBR'].nunique())

