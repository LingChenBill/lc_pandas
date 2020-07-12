#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/14
# @Author: Lingchen
# @Prescription: 在DataFrame上使用运算符
import pandas as pd

college = pd.read_csv('../data/college.csv')

# college数据集的值既有数值也有对象，整数不能与字符串相加
# TypeError: can only concatenate str (not "int") to str
# print(college + 5)

# 查看前5行
print(college.head())

# 行索引名设为INSTNM, 用UGDS_过滤出本科生的种族比例
college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds = college.filter(like='UGDS_')
print(college_ugds.head())

# 现在都是均质数据，可以进行数值运算了
print(college_ugds.head() + .00501)

# 用底除计算百分比分数
print((college_ugds.head() + .00501) // .01)

# 再除以100
college_ugds_op_round = (college_ugds + .00501) // .01 / 100
print(college_ugds_op_round.head())

# 保留两位小数
college_ugds_round = (college_ugds + .00001).round(2)
print(college_ugds_round.head())

print(.045 + .005)

print(college_ugds_op_round.equals(college_ugds_round))
