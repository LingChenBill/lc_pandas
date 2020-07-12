#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/9
# @Author: Lingchen
# @Prescription: 翻译SQL的where
import pandas as pd

print('读取employee数据集：')
employee = pd.read_csv('../data/employee.csv')
print('对各项进行了解：')
print(employee.DEPARTMENT.value_counts().head())
print(employee.GENDER.value_counts().head())
print(employee.BASE_SALARY.describe().astype(int))

print('创建布尔条件，从四列中选取数据：')
depts = ['Houston Police Department-HPD', 'Houston Fire Department (HFD)']
criteria_dept = employee.DEPARTMENT.isin(depts)
criteria_gender = employee.GENDER == 'Female'
criteria_sal = (employee.BASE_SALARY >= 80000) & (employee.BASE_SALARY <= 120000)
criteria_final = criteria_dept & criteria_gender & criteria_sal
select_cols = ['DEPARTMENT', 'GENDER', 'BASE_SALARY']
print(employee.loc[criteria_final, select_cols].head())

print('使用 between 选取80000 到120000之间的薪水：')
criteria_sal = employee.BASE_SALARY.between(80000, 120000)
print('排队最长出现的的5家单位：')
top_5_depts = employee.DEPARTMENT.value_counts().index[:5]
criteria = ~employee.DEPARTMENT.isin(top_5_depts)
print(employee[criteria].head())
