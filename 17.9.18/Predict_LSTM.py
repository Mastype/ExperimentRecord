# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:43:23 2017

使用LSTM 进行 股指数据的预测
股指为 S&P500

@author: dell
"""
import pandas
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.contrib import learn
from sklearn.metrics import mean_squared_error

from lstm import lstm_model
import data_processing 


dataframe = pandas.read_csv('Data/S&P500.csv')
# 进行单变量的预测过程
closeprices = dataframe['Close Price']
#标准化过程 ，不能使用全部数据进行标准化。
n_scaler = MinMaxScaler(feature_range=(0, 1))
n_scaler = n_scaler.fit(closeprices)
n_cp = n_scaler.transform(closeprices)

origin = np.array(n_cp[0:(len(dataframe)-1)])
label = np.array(n_cp[1:])
data = dict(a=origin, b=label)


#参数定义
LOG_DIR = './ops_logs/S&P500_LSTM'   # 日志文件
TIMESTEPS = 3                # 预测的时间步长
RNN_LAYERS = [{'num_units': 5}] 
DENSE_LAYERS = None
TRAINING_STEPS = 10000
PRINT_STEPS = TRAINING_STEPS / 10
BATCH_SIZE = 5

#数据分割
X1, Y1 = data_processing.load_csvdata(data, TIMESTEPS, True)

# 建立模型
regressor =  learn.SKCompat(learn.Estimator(
    model_fn=lstm_model(
        TIMESTEPS,
        RNN_LAYERS,
        DENSE_LAYERS
    ),
    model_dir=LOG_DIR
))

#建立模型实例和验证因子。
validation_monitor = learn.monitors.ValidationMonitor(X1['val'], Y1['val'],
                                                     every_n_steps=PRINT_STEPS,
                                                     early_stopping_rounds=1000)
regressor.fit(X1['train'], Y1['train'], 
              monitors=[validation_monitor], 
              batch_size=BATCH_SIZE,
              steps=TRAINING_STEPS)


predicted = regressor.predict(X1['test'])
rmse = np.sqrt(((predicted - Y1['test']) ** 2).mean(axis=0))
score = mean_squared_error(predicted, Y1['test'])
print ("MSE: %f" % score)
plot_predicted, = plt.plot(predicted, label='predicted')
plot_test, = plt.plot(Y1['test'], label='test')
plt.legend(handles=[plot_predicted, plot_test])