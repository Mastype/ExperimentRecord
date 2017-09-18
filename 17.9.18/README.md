#股指预测实验重现
参考论文：（Bao W, Yue J, Rao Y. A deep learning framework for financial time series using stacked autoencoders and long-short term memory[J]. PloS one, 2017, 12(7): e0180944.）

---
###数据源：[股指数据](figshare.com/s/acdfb4918c0695405e33) （RawData.xlsx）
每个市场包含2类数据 一个是index data 另一个是index future data 用于对比实验。

不同市场间的数据在时间维度上具有差别。CSI300 没有宏观经济因子。

---
###小波变换

文中的描述：When the financial time series is very rough, the discrete wavelet transformation can be applied repeatedly by which the risk of overfitting can be reduced. As a result,  **the two-level wavelet is applied twice** in this study for data preprocessing.

文中小波变换的过程参考的是
[Forecasting stock markets using wavelet transforms and recurrent neural
networks: An integrated system based on artificial bee colony algorithm]()

python 小波变换库 Pywalvets。[Pywalvets 学习笔记](http://blog.csdn.net/nanbei2463776506/article/details/64124841)

---
### SAE 结构

[自编码器之间的差异](https://www.zhihu.com/question/41490383)

[Stacked Auto-Encoder搭建](https://www.cnblogs.com/tornadomeet/archive/2013/04/09/3011209.html)

[2号模型](http://blog.csdn.net/freeliao/article/details/19618855)

[3号模型 使用Tensorflow实现Denoising Auto-Encoder](http://blog.csdn.net/u013719780/article/details/53908852)

---

### LSTM结构


---

###混合模型