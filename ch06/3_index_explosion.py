#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/14
# @Author: Lingchen
# @Prescription: 索引爆炸
import pandas as pd

print('读取数据集，设定 RACE 为行索引：')
employee = pd.read_csv('../data/employee.csv', index_col='RACE')
print(employee.head())

print('选取 BASE_SALARY 做成两个 Series, 判断两者是否相等：')
salary1 = employee['BASE_SALARY']
salary2 = employee['BASE_SALARY']
print(salary1 is salary2)

print('选取 BASE_SALARY 做成两个 Series, 使用 copy 方法，判断两者是否相等：')
salary1 = employee['BASE_SALARY'].copy()
salary2 = employee['BASE_SALARY'].copy()
print(salary1 is salary2)

print('对其中一个进行索引排序，比较二者是否相等：')
salary1 = salary1.sort_index()
print(salary1.head())
print('未排序：')
print(salary2.head())

print('将两个 Series 进行相加：')
salary_add = salary1 + salary2
print(salary_add.head())

print('将 salary1 进行自身相加，查看几个Series的长度：')
salary_add1 = salary1 + salary1
print(len(salary1), len(salary2), len(salary_add), len(salary_add1))

print('验证 salary_add 的个数，因为笛卡尔积作用相同索引元素上，可以对其平方值求和：')
index_vc = salary1.index.value_counts(dropna=False)
print(index_vc)
print('平方值求和：')
print(index_vc.pow(2).sum())
