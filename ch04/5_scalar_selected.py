#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/4
# @Author: Lingchen
# @Prescription: 快速选取标量
import pandas as pd
import time

college = pd.read_csv('data/college.csv', index_col='INSTNM')

print('通过将行标签赋值于一个变量，用loc选取：')
cn = 'Texas A & M University-College Station'
start = time.perf_counter()
print(college.loc[cn, 'UGDS_WHITE'])
stop = time.perf_counter()
print('Time1: ', stop - start)

print('at可以实现相同的功能：')
start = time.perf_counter()
print(college.at[cn, 'UGDS_WHITE'])
stop = time.perf_counter()
print('Time2: ', stop - start)

print('.iat和.at 只接收标量值，是专门用来取代.iloc和.loc选取标量的，可以节省时间')

print('用get_loc来找到整数位置，再进行速度比较：')
row_num = college.index.get_loc(cn)
col_num = college.columns.get_loc('UGDS_WHITE')
print(row_num, col_num)

start = time.perf_counter()
print(college.iloc[row_num, col_num])
stop = time.perf_counter()
print('Time3: ', stop - start)

start = time.perf_counter()
print(college.iat[row_num, col_num])
stop = time.perf_counter()
print('Time4: ', stop - start)

print('Series对象也可以使用.iat和.at选取标量：')
state = college['STABBR']
print(state)
print(state.iat[1000])
print(state.at['Hot Springs Beauty College'])




