#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/27
# @Author: Lingchen
# @Prescription: 同时选取Dataframe的行和列
import pandas as pd

print('选取前3行与前4列：')
college = pd.read_csv('data/college.csv', index_col='INSTNM')
print(college.iloc[:3, :4])

print('用loc来实现选取前3行与前4列：')
print(college.loc[:'Amridge University', :'MENONLY'])

print('选取两列的所有行：')
print(college.iloc[:, [4, 6]].head())

print('用loc选取两列的所有行：')
print(college.loc[:, ['WOMENONLY', 'SATVRMID']].head())

print('选取不连续的行和列：')
print(college.iloc[[100, 200], [7, 15]])

print('用loc和列表，来选取不连续的行和列：')
rows = ['GateWay Community College', 'American Baptist Seminary of the West']
cols = ['SATMTMID', 'UGDS_NHPI']
print(college.loc[rows, cols])

print('选取一个标量值：')
print(college.iloc[5, -4])

print('loc选取一个标量值：')
print(college.loc['The University of Alabama', 'PCTFLOAN'])

print('iloc对行切片，并只选取一列：')
print(college.iloc[90:80:-2, 5])

print('loc对行切片，并只选取一列：')
start = 'Empire Beauty School-Flagstaff'
stop = 'Arizona State University-Tempe'
print(college.loc[start:stop:-2, 'RELAFFIL'])




