#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/8/24
# @Author: Lingchen
# @Prescription: 减肥对赌（page_186）
import pandas as pd
import numpy as np

print('读取减肥数据集，查看一月的数据：')
weight_loss = pd.read_csv('../data/weight_loss.csv')
print(weight_loss.query('Month == "Jan"'))


def find_perc_loss(s):
    """
    定义一个求减肥比例的函数
    :param s:
    :return:
    """
    return (s - s.iloc[0]) / s.iloc[0]


print('查看Bob在一月的减肥成果：')
bob_jan = weight_loss.query('Name == "Bob" and Month == "Jan"')
print(find_perc_loss(bob_jan['Weight']))

print('对Name和Month进行分组，然后使用transform方法，传入函数，对数值进行转换：')
pcnt_loss = weight_loss.groupby(['Name', 'Month'])['Weight'].transform(find_perc_loss)
print(pcnt_loss.head(8))

print('transform之后的结果，行数不变，可以赋值给原始DataFrame作为一个新列：')
print('为了缩短输出，只选择Bob的前两个月数据：')
weight_loss['Perc Weight Loss'] = pcnt_loss.round(3)
print(weight_loss.query('Name == "Bob" and Month in ["Jan", "Feb"]'))

print('因为最重要的是每个月的第4周，只选择第4周的数据：')
week4 = weight_loss.query('Week == "Week 4"')
print(week4)

print('用 pivot 重构DataFrame, 让Amy 和 Bob的数据并排放置：')
winner = week4.pivot(index='Month', columns='Name', values='Perc Weight Loss')
print(winner)

print('用 where 方法选出每月的赢家：')
winner['Winner'] = np.where(winner['Amy'] < winner['Bob'], 'Amy', 'Bob')
winner.style.highlight_min(axis=1)
print(winner)

print('用 value_counts() 返回最后的比分：')
print(winner.Winner.value_counts())

print('Pandas默认是按字母排序的：')
week4a = week4.copy()
month_chron = week4a['Month'].unique()
print(month_chron)

print('转换为 Categorical 变量，可以做成按时间排序：')
week4a['Month'] = pd.Categorical(week4a['Month'], categories=month_chron, ordered=True)
print(week4a.pivot(index='Month', columns='Name', values='Perc Weight Loss'))

