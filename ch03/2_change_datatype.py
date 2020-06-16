#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/16
# @Author: Lingchen
# @Prescription: 改变数据类型，降低内存消耗
import pandas as pd
import numpy as np

# 选取5列
college = pd.read_csv('data/college.csv')
different_cols = ['RELAFFIL', 'SATMTMID', 'CURROPER', 'INSTNM', 'STABBR']
col2 = college.loc[:, different_cols]
print(col2.head())

# 查看数据类型
print(col2.dtypes)

# 用 memory_usage 方法查看每列的内存消耗
original_mem = col2.memory_usage(deep=True)
print(original_mem)

# RELAFFIL这列只包含0或1，因此没有必要用64位，使用astype方法将其变为8位（1字节）整数
col2['RELAFFIL'] = col2['RELAFFIL'].astype(np.int8)
print(col2.dtypes)

# 检查两个对象列的独立值的个数
print(col2.select_dtypes(include=['object']).nunique())

# STABBR列可以转变为"类型"（Categorical），独立值的个数小于总数为1%
col2['STABBR'] = col2['STABBR'].astype('category')
print(col2.dtypes)

# 再次检查内存的使用
new_mem = col2.memory_usage(deep=True)
print(new_mem)

# 与原始内存进行比较
print(new_mem / original_mem)

# 查看CURROPER列 和 INSTNM列的类型
print(college[['CURROPER', 'INSTNM']].memory_usage(deep=True))

college.loc[0, 'CURROPER'] = 10000000
college.loc[0, 'INSTNM'] = college.loc[0, 'INSTNM'] + 'a'

print(college[['CURROPER', 'INSTNM']].memory_usage(deep=True))

# 查看 列的类型
print(college['MENONLY'].dtype)

# 由于含有缺失值，类型转换出错
# ValueError: Cannot convert non-finite values (NA or inf) to integer
# college['MENONLY'].astype('int8')

# 对于类型，可以替换字符串名
print(college.describe(include=['int64', 'float64']).T)
print(college.describe(include=[np.int64, np.float64]).T)

print(college.dtypes)
college['RELAFFIL'] = college['RELAFFIL'].astype(np.int8)
print(college.dtypes)
print(college.describe(include=['int', 'float']).T)

# 显示number 类型
print(college.describe(include=['number']).T)
