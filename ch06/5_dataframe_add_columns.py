#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/8/18
# @Author: Lingchen
# @Prescription: 从不同的DataFrame追加列（page_145）
import pandas as pd
import numpy as np

employee = pd.read_csv('../data/employee.csv')
dept_sal = employee[['DEPARTMENT', 'BASE_SALARY']]

print('在每个部门内，对BASE_SALARY进行排序：')
dept_sal = dept_sal.sort_values(['DEPARTMENT', 'BASE_SALARY'], ascending=[True, False])
print('用 drop_duplicates 方法保留每个部门的第一行：')
max_dept_sal = dept_sal.drop_duplicates(subset='DEPARTMENT')
print(max_dept_sal.head())

print('使用 DEPARTMENT 作为行索引：')
max_dept_sal = max_dept_sal.set_index('DEPARTMENT')
employee = employee.set_index('DEPARTMENT')

print('现在行索引包含匹配值了，可以向 employee 的 DataFrame 新增一列：')
employee['MAX_DEPT_SALARY'] = max_dept_sal['BASE_SALARY']
pd.options.display.max_columns = 6
print('现在可以用 query 查看是否有BASE_SALARY 大于 MAX_DEPT_SALARY 的：')
print(employee.query('BASE_SALARY > MAX_DEPT_SALARY'))

print('用 random 从 dept_sal 随机取10行，不做替换：')
np.random.seed(1234)
random_salary = dept_sal.sample(n=10).set_index('DEPARTMENT')
print(random_salary)

print('有重复的索引：cannot reindex from a duplicate axis')
# employee['RANDOM_SALARY'] = random_salary['BASE_SALARY']

print("选取 max_dept_sal['BASE_SALARY'] 的前三行，赋值给 employee['MAX_SALARY2'] ")
employee['MAX_SALARY2'] = max_dept_sal['BASE_SALARY'].head(3)
print('对MAX_SALARY2统计：')
print(employee.MAX_SALARY2.value_counts())

print('因为只填充了三个部门的值，所有其它部门在结果中都是缺失值: ')
print(employee.MAX_SALARY2.isnull().mean())
