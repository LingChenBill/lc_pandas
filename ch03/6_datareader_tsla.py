#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/27
# @Author: Lingchen
# @Prescription: 计算跟踪止损单价格
#    pip install pandas_datareader
import pandas_datareader as pdr

print('tsla, 读取google源时可能出错，切换到yahoo源: ')
tsla = pdr.DataReader('tsla', data_source='yahoo', start='2017-1-1')
print(tsla.head(8))

print('只关注每天的收盘价，使用cummax得到迄今为止的收盘价最大值：')
tsla_close = tsla['Close']
tsla_cummax = tsla_close.cummax()
print(tsla_cummax.head(8))

print('将下行区间限制到10%，将tsla_cummax乘以0.9：')
tsla_training_stop = tsla_cummax * .9
print(tsla_training_stop.head(8))

