# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:16:24 2021

@author: 电脑
"""
# 叠加柱状图
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['font.family'] = 'SimHei'

# #加载原始数据
# csv = pd.read_csv("D:\\1123.csv")
# # print(csv)
# # print(csv.columns)
# l=6
# lis=[1]*l
# x=[x for x in range(1,7)]
# y = csv['1FRR_0'].values[0:7]
# y = list(y)
# y1 = csv['1FRR_retry0'].values[0:7]
# y1 = list(y1)
# y2 = csv['1FRR_retry1'].values[0:7]
# y2 = list(y2)
# y3 = csv['1FRR_retry2'].values[0:7]
# y3 = list(y3)
# #获得数据标签
# v1 = list(map(lambda x: x[0]-x[1], zip(lis, y)))
# v1 = np.array(v1)                    #列表转数组
# v1 = np.round(v1,5)                 #对数组中的元素保留5位小数
# v1 = list(v1)                     #数组转列表
# #print(v1)
# v2 = list(map(lambda x: x[0]-x[1], zip(v1, y1)))
# v2 = np.array(v2)
# v2 = np.round(v2,5)
# v2 = list(v2)
# # print(v2)
# v3 = list(map(lambda x: x[0]-x[1], zip(v2, y2)))
# v3 = np.array(v3)
# v3 = np.round(v3,5)
# v3 = list(v3)
# # print(v3)
# v4 = list(map(lambda x: x[0]-x[1], zip(v3, y3)))
# v4 = np.array(v4)
# v4 = np.round(v4,5)
# v4 = list(v4)
# # print(v4)
# f1 = list(map(lambda x: x[0]-x[1], zip(v3, v4)))
# f1 = np.array(f1)                    #列表转数组
# f1 = np.round(f1,5)                 #对数组中的元素保留5位小数
# f1 = list(f1)                     #数组转列表
# print(f1)
# f2 = list(map(lambda x: x[0]-x[1], zip(v2, v3)))
# f2 = np.array(f2)
# f2 = np.round(f2,5)
# f2 = list(f2)
# print(f2)
# f3 = list(map(lambda x: x[0]-x[1], zip(v1, v2)))
# f3 = np.array(f3)
# f3 = np.round(f3,5)
# f3 = list(f3)
# print(f3)
# list=[v4,f1,f2,f3]
# list = zip(*list)
# name=['FRR_retry2', 'FRR_retry1', 'FRR_retry0','FRR_0']
# name2=['1634_12_14','1635_12_14','1634_12_21','1635_12_21','1634_1_1','1635_1_1']
# test=pd.DataFrame(columns=name,index=name2,data=list)
# print(test)
# test.to_csv('E:/testcsv.csv',encoding='gbk')  #保存计算过后数据
# #加载计算过后数据数据
# csv1 = pd.read_csv("E:\\testcsv.csv")
# # 获取y轴的数据表头
# csv1.plot.bar(y=['FRR_retry2', 'FRR_retry1', 'FRR_retry0','FRR_0'], color=['blue', 'yellow','brown','red'], stacked=True)
# # 设置x轴的排列顺序为csv中的index
# plt.xticks(csv1.index ,('1634_12_14','1635_12_14','1634_12_21','1635_12_21','1634_1_1','1635_1_1'),rotation=0, fontsize=10)

# for x,v1,v2,v4,v3  in zip(x,v1,v2,v4,v3):
#     plt.text(x-1 ,v1, v1, ha='center', va='bottom')
#     plt.text(x-1 ,v2, v2, ha='center', va='bottom')
#     plt.text(x-1 ,v4, v4, ha='center', va='bottom')
#     plt.text(x-1 ,v3, v3, ha='center', va='bottom')
# # # plt.text(0.0, 0.31, 0.9361, ha='center', rotation=15, wrap=True,color=(0.1, 0.2, 0.5))

# plt.title('retry4', fontsize=16, fontweight='bold')
# plt.ylabel('FRR', fontsize=12)
# plt.xlabel('finger(ID)', fontsize=12)
# plt.legend(loc= 'best',frameon=False,fontsize = 'small')
# plt.show()



######################################################################################################################


csv = pd.read_csv(r"D:\\f1635.csv",skiprows=1,nrows=55)
#csv1 = pd.read_csv("D:\DC47D758-4806-4187-858C-1D88BDDE2503.csv",skiprows=1+6,nrows=5)
# print(csv)
# print(csv.columns)
mpl.rcParams['font.family'] = 'SimHei'
l = 55
lis=[1]*l
y = csv['FRR_0'].values[0:57]
y = list(y)
y1 = csv['FRR_1'].values[0:57]
y1 = list(y1)
y2 = csv['FRR_2'].values[0:57]
y2 = list(y2)
y3 = csv['FRR_3'].values[0:57]
y3 = list(y3)

# number = 55
# y = np.zeros(number)
# y1 = np.zeros(number)
# y2 = np.zeros(number)
# y3 = np.zeros(number)
# for i in range(number):
#     y[i] = float(y[i].strip('%'))/100
#     y1[i] = float(y[i].strip('%'))/100
#     y2[i] = float(y[i].strip('%'))/100
#     y3[i] = float(y[i].strip('%'))/100

#获得数据标签
v1 = list(map(lambda x: x[0]-x[1], zip(lis, y)))
v1 = np.array(v1)                    #列表转数组
v1 = np.round(v1,5)                 #对数组中的元素保留两位小数
v1 = list(v1)                     #数组转列表
#print(v1)
v2 = list(map(lambda x: x[0]-x[1], zip(v1, y1)))
v2 = np.array(v2)
v2 = np.round(v2,5)
v2 = list(v2)
#print(v2)
v3 = list(map(lambda x: x[0]-x[1], zip(v2, y2)))
v3 = np.array(v3)
v3 = np.round(v3,5)
v3 = list(v3)
#print(v3)
v4 = list(map(lambda x: x[0]-x[1], zip(v3, y3)))
v4 = np.array(v4)
v4 = np.round(v4,5)
v4 = list(v4)
#print(v4)

f1 = list(map(lambda x: x[0]-x[1], zip(v3, v4)))
f1 = np.array(f1)                    #列表转数组
f1 = np.round(f1,5)                 #对数组中的元素保留两位小数
f1 = list(f1)                     #数组转列表
#print(f1)
f2 = list(map(lambda x: x[0]-x[1], zip(v2, v3)))
f2 = np.array(f2)
f2 = np.round(f2,5)
f2 = list(f2)
#print(f2)
f3 = list(map(lambda x: x[0]-x[1], zip(v1, v2)))
f3 = np.array(f3)
f3 = np.round(f3,5)
f3 = list(f3)
#print(f3)
list=[v4,f1,f2,f3]
list = zip(*list)
name=['FRR_3', 'FRR_2', 'FRR_1', 'FRR_0']
name2=['L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3']
test = pd.DataFrame(columns=name,index=name2,data=list)
print(test)
test.to_csv('E:/testcsv.csv',encoding='gbk')  #保存计算过后数据
#加载计算过后数据数据
csv1 = pd.read_csv("E:\\testcsv.csv")
# 获取y轴的数据表头
csv1.plot.bar(y=['FRR_3', 'FRR_2', 'FRR_1', 'FRR_0'], color=['blue', 'yellow','brown','red'], stacked=True)
# 设置x轴的排列顺序为csv中的index
plt.xticks(csv1.index ,('L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3',
                        'L1','L2','R1','R2','R3'), fontsize=6)
#plt.xticks(csv.index ,('L1','L2','R1','R2','R3'), fontsize=12)
plt.title('1635retry1 21', fontsize=16, fontweight='bold')
plt.ylabel('FRR', fontsize=12)
plt.xlabel('finger(ID)', fontsize=12)
plt.legend(loc= 'best',frameon=False,fontsize = 'small')
plt.show()






















