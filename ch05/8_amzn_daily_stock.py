#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/11
# @Author: Lingchen
# @Prescription: 确定股票收益的正态值
import pandas as pd
import matplotlib.pyplot as plt

amzn = pd.read_csv('../data/amzn_stock.csv', index_col='Date', parse_dates=['Date'])
print('加载亚马逊的股票，使用 Date 作为行索引：')
print(amzn.head())

print('选取 Close 收盘价，用 pct_change 计算每日回报率：')
amzn_daily_return = amzn.Close.pct_change()
print(amzn_daily_return.head())

print('去掉缺失值，画一张柱状图，查看分布情况：')
amzn_daily_return = amzn_daily_return.dropna()
amzn_daily_return.hist(bins=20)
# plt.show()

print('计算平均值和标准差: ')
mean = amzn_daily_return.mean()
std = amzn_daily_return.std()
print('mean: ', mean)
print('std: ', std)

print('计算每个数据的 z-score 的绝对值：z-score 是远离平均值的标准差值的个数：')
abs_z_score = amzn_daily_return.sub(mean).abs().div(std)
print('abs_z_score: ', abs_z_score)

print('计算位于1，2， 3个标准差之内的收益率的比例：')
pcts = [abs_z_score.lt(i).mean() for i in range(1, 4)]
print('{:.3f} fall within 1 standard deviation. '
      '{:.3f} within 2 and {:.3f} within 3'.format(*pcts))

print('将上面的方法整合成一个函数：')


def test_return_normality(stock_data):
    """
    计算位于1，2， 3个标准差之内的收益率的比例
    :param stock_data:
    :return:
    """
    close = stock_data['Close']
    # 计算每日回报率
    daily_return = close.pct_change().dropna()
    daily_return.hist(bins=20)
    # 平均值
    mean = daily_return.mean()
    # 标准差
    std = daily_return.std()
    # abs_z_score 远离平均值的标准差值的个数
    abs_z_score = abs(daily_return - mean) / std
    # 计算位于1，2， 3个标准差之内的收益率的比例
    pcts = [abs_z_score.lt(i).mean() for i in range(1, 4)]
    print('{:.3f} fall within 1 standard deviation. '
          '{:.3f} within 2 and {:.3f} within 3'.format(*pcts))


slb = pd.read_csv('../data/slb_stock.csv', index_col='Date', parse_dates=['Date'])
test_return_normality(slb)
