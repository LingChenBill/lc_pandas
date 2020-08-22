#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/8/22
# @Author: Lingchen
# @Prescription: 用 args 和 *kwargs 自定义聚合函数（page_175）
import pandas as pd
import inspect

print('用 inspect 模块来查看 groupby 对象的agg方法的签名：')
college = pd.read_csv('../data/college.csv')
grouped = college.groupby(['STABBR', 'RELAFFIL'])
print(inspect.signature(grouped.agg))

print('自定义一个返回去本科生人数在1000 和 3000 之间的比例的函数：')


def pct_between_1_3k(s):
    """
    自定义一个返回去本科生人数在1000 和 3000 之间的比例的函数
    :param s:
    :return:
    """
    return s.between(1000, 3000).mean()


print('用州和宗教分组，再聚合：')
print(college.groupby(['STABBR', 'RELAFFIL'])['UGDS'].agg(pct_between_1_3k).head(9))

print('但是这个函数不能让用户自定义上下限，再新写一个函数：')


def pct_between(s, low, high):
    return s.between(low, high).mean()


print('使用这个自定义聚合函数，并传入最大和最小值：')
print(college.groupby(['STABBR', 'RELAFFIL'])['UGDS'].agg(pct_between, 1000, 10000).head(9))

print('显示指定最大和最小值：')
print(college.groupby(['STABBR', 'RELAFFIL'])['UGDS'].agg(pct_between, high=10000, low=1000).head(9))

print('也可以关键字参数与非关键字参数混合使用，只要非关键字参数在后面：')
print(college.groupby(['STABBR', 'RELAFFIL'])['UGDS'].agg(pct_between, 1000, high=10000).head(9))

print('Pandas不支持多重聚合时，使用参数：')
print("pct_between() missing 2 required positional arguments: 'low' and 'high'")
# print(college.groupby(['STABBR', 'RELAFFIL'])['UGDS'].agg(['mean', pct_between], low=1000, high=10000).head(9))

print('用闭包自定义聚合函数：')


def make_agg_func(func, name, *args, **kwargs):
    def wrapper(x):
        return func(x, *args, **kwargs)
    wrapper.__name__ = name
    return wrapper


my_agg1 = make_agg_func(pct_between, 'pct_1_3k', low=1000, high=3000)
print("'function' object is not subscriptable: ")
print(make_agg_func(pct_between, 'pct_10_30k', 10000, 30000)['UGDS'].agg(pct_between, 1000, high=10000).head(9))

