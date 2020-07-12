#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/9
# @Author: Lingchen
# @Prescription: 观察股价
import pandas as pd
import matplotlib.pyplot as plt

slb = pd.read_csv('../data/slb_stock.csv', index_col='Date', parse_dates=['Date'])
print('股价行索引设为Date, 并将其转变为DateTime: ')
print(slb.head())

print('选取 Close 列，显示统计信息：')
slb_close = slb['Close']
slb_summary = slb_close.describe(percentiles=[.1, .9])
print(slb_summary)

print('用布尔索引选取最高和最低的10%的收盘价：')
upper_10 = slb_summary.loc['90%']
lower_10 = slb_summary.loc['10%']
criteria = (slb_close < lower_10) | (slb_close > upper_10)
slb_top_bottom_10 = slb_close[criteria]
print(slb_top_bottom_10)

print('过滤出的数据显示灰色，所有收盘价使用黑色，用 matploylib 在十分之一和十分之九位数位置划横线：')
slb_close.plot(color='black', figsize=(10, 6))
slb_top_bottom_10.plot(marker='o', style=' ', ms=4, color='lightgray')
xmin = criteria.index[0]
xmax = criteria.index[-1]
plt.hlines(y=[lower_10, upper_10], xmin=xmin, xmax=xmax, color='black')
plt.show()

print('使用 fill_between 可以在两条线之间填充黑色：')
slb_close.plot(color='black', figsize=(10, 6))
plt.hlines(y=[lower_10, upper_10], xmin=xmin, xmax=xmax, color='lightgray')
plt.fill_between(x=criteria.index, y1=lower_10, y2=slb_close.values, color='black')
plt.fill_between(x=criteria.index, y1=lower_10, y2=slb_close.values, where=slb_close < lower_10, color='lightgray')
plt.fill_between(x=criteria.index, y1=upper_10, y2=slb_close.values, where=slb_close > upper_10, color='lightgray')
plt.show()
