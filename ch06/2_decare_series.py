#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/13
# @Author: Lingchen
# @Prescription: 求笛卡尔积
import pandas as pd
import numpy as np

print('创建两个有不同索引，但包含一些相同值的Series: ')
s1 = pd.Series(index=list('aaab'), data=np.arange(4))
print(s1)

s2 = pd.Series(index=list('cababb'), data=np.arange(6))
print(s2)

print('二者相加，产生一个笛卡尔积：')
print(s1 + s2)

print('当两组元素相同，顺序也相同，不会生成笛卡尔积，索引会按照它们的位置对齐：')
s3 = pd.Series(index=list('aaabb'), data=np.arange(5))
s4 = pd.Series(index=list('aaabb'), data=np.arange(5))
print(s3 + s4)

print('若索引元素相同，但顺序不同，会产生笛卡尔积：')
s5 = pd.Series(index=list('aaabb'), data=np.arange(5))
s6 = pd.Series(index=list('bbaaa'), data=np.arange(5))
print(s5 + s6)
