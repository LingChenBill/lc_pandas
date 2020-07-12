#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/12
# @Author: Lingchen
# @Prescription: 使用查询方法提高布尔索引的可读性
import pandas as pd

employee = pd.read_csv('../data/employee.csv')
depts = ['Houston Police Department-HPD', 'Houston Fire Department (HFD)']
select_columns = ['DEPARTMENT', 'GENDER', 'BASE_SALARY']

print('创建查询字符串，并执行query方法：')
qs = "DEPARTMENT in @depts " \
    "and GENDER == 'Female' " \
    "and 80000 <= BASE_SALARY <= 120000"

emp_filtered = employee.query(qs)
print(emp_filtered[select_columns].head())

print('若不想使用部门列表，也可以使用方法：')
top10_depts = employee.DEPARTMENT.value_counts().index[:10].tolist()
qs = "DEPARTMENT not in @top10_depts and GENDER == 'Female'"
emp_filtered2 = employee.query(qs)
print(emp_filtered2[['DEPARTMENT', 'GENDER']].head())
