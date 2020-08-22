#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/8/22
# @Author: Lingchen
# @Prescription: 检查分组对象（page_180）
import pandas as pd
from IPython.display import display

print('查看分组对象的类型：')
college = pd.read_csv('../data/college.csv')
grouped = college.groupby(['STABBR', 'RELAFFIL'])
print(type(grouped))

print('用 dir 函数找到该对象所有的可用函数：')
print([attr for attr in dir(grouped) if not attr.startswith('_')])

print('用 ngroups 属性查看分组的数量：')
print(grouped.ngroups)

print('查看每个分组的唯一识别标签，groups 属性是一个字典，包含每个独立分组和行索引标签的对应：')
groups = list(grouped.groups.keys())
print(groups[:6])

print('用 get_group, 传入分组标签的元组，例如，获取佛罗里达州所有与宗教有关的学校：')
print(grouped.get_group(('FL', 1)).head())

print('groupby 对象是一个可迭代对象，可以挨个查看每个独立分组：')
i = 0
for name, group in grouped:
    print(name)
    display(group.head(2))
    i += 1
    if i == 5:
        break

print('groupby 对象使用head 方法，可以在一个 DataFrame 中显示每个分组的头几行：')
print(grouped.head(2).head(6))

print('nth 方法可以选出每个分组指定行的数据，下面选出的是第1行和最后1行：')
print(grouped.nth([1, -1]).head(8))
