#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/16
# @Author: Lingchen
# @Prescription: 规划数据分析路线
import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50

# 读取数据
college = pd.read_csv('../data/college.csv')
print(college.head())

# 数据的行数与列数
print(college.shape)

# 统计数值列，并进行转置
with pd.option_context('display.max_rows', 8):
    display(college.describe(include=[np.number]).T)

# 统计对象和类型列
print(college.describe(include=[np.object, pd.Categorical]).T)

# 列出每列的数据类型，非缺失值的数量，以及内存的使用
print(college.info())

# 不设置最大行数
print(college.describe(include=[np.number]).T)

# 在describe方法中，打印分位数
with pd.option_context('display.max_rows', 5):
    display(college.describe(include=[np.number],
                             percentiles=[.01, .05, .10, .25, .5, .75, .9, .95, .99]).T)

# 展示一个数据字典：数据字典的主要作用是解释列名的意义
college_dd = pd.read_csv('../data/college_data_dictionary.csv')
with pd.option_context('display.max_rows', 8):
    display(college_dd)
