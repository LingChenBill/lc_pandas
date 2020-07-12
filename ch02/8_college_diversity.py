#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/14
# @Author: Lingchen
# @Prescription: 确定大学校园多样性
import pandas as pd

college = pd.read_csv('../data/college.csv', index_col='INSTNM')
college_ugds = college.filter(like='UGDS_')
print(college_ugds.head())

print(college_ugds.isnull().sum(axis=1).sort_values(ascending=False).head())

# 如果所有列都是缺失值，则将其去除
college_ugds = college_ugds.dropna(how='all')
print(college_ugds.isnull().sum())

# 用大于或等于方法ge()，将DataFrame变为布尔值矩阵
print(college_ugds.ge(.15).head())

# 对所有True值求和
diversity_metric = college_ugds.ge(.15).sum(axis='columns')
print(diversity_metric.head())

# 使用value_counts(),查看分布情况
print(diversity_metric.value_counts())

# 降序排列
print(diversity_metric.sort_values(ascending=False).head())

# 使用loc()方法查看对应行索引的行,loc是方括号
print(college_ugds.loc[['Regency Beauty Institute-Austin',
                        'Central Texas Beauty College-Temple']])

# 查看US News前五所最具多样性的大学在diversity_metric中的情况
us_news_top = ['Rutgers University-Newark',
               'Andrews University',
               'Stanford University',
               'University of Houston',
               'University of Nevada-Las Vegas']
print(diversity_metric.loc[us_news_top])

# 可以用最大种群比例查看哪些学校最不具有多样性
print(college_ugds.max(axis=1).sort_values(ascending=False).head(10))

# 查看Talmudical Seminary Oholei Torah 哲学学校
print(college_ugds.loc['Talmudical Seminary Oholei Torah'])

# 查看是否有学校九个种族的比例都超过了1%
print((college_ugds > .01).all(axis=1).any())
