#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/27
# @Author: Lingchen
# @Prescription: 选取Series数据
import pandas as pd
import numpy as np

print('读取college数据集，查看CITY的前5行：')
college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']
print(city.head())

print('可以通过整数选取：')
print(city.iloc[3])

print('可以通过整数列表来选取多行，返回结果是Series：')
print(city.iloc[[10, 20, 30]])

print('选取等分的数据，可以使用切片语法：')
print(city.iloc[4:50:10])

print('只接收行索引标签：')
print(city.loc['Heritage Christian University'])

print('随机选择4个标签：')
np.random.seed(1)
labels = list(np.random.choice(city.index, 4))
print(labels)

print('通过标签列表选择多行：')
print(city.loc[labels])

print('可以通过切片语法均匀选择多个：')
print(city.loc['Alabama State University':'Reid State Technical College':10])

print('也可以使用纯python语法：')
print(city['Alabama State University':'Reid State Technical College':10])

print('要想只选择一项，并保留其Series类型，则传入一个只包含一项的列表')
print(city[[3]])

print('也可以切片逆序选取：')
print(city.loc['Reid State Technical College': 'Alabama State University':-10])




