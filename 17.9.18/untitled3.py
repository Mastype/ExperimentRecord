# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 18:59:57 2017

数据读入：
当前仅测试两组数据 S&P 500 和 CJIA。

@author: dell
"""
from pandas import DataFrame
import pandas 
#小波变换库
import pywt
from matplotlib import pyplot

dataframe = pandas.read_csv('Data/S&P500.csv')

data080701 = dataframe[['Ntime','Close Price']][(dataframe.Ntime > 20080630) & (dataframe.Ntime < 20100701)]
data11 = DataFrame(data080701['Close Price'])

#小波模型的创建
haar = pywt.Wavelet('haar')
# 分解
cS2,cD2,cD1 = pywt.wavedec(data080701['Close Price'], haar, level = 2)
# 重建
data11['C_DWT']= pywt.waverec([cS2,None,None], haar)
data11.plot()
pyplot.show()