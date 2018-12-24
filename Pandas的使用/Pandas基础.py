import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""
1. 数据结构
Pandas处理以下三个数据结构 
- 系列(Series)
- 数据帧(DataFrame)
- 面板(Panel)
"""


# 1.1 系列
# 系列(Series)是能够保存任何类型的数据(整数，字符串，浮点数，Python对象等)的一维标记数组。轴标签统称为索引。

# Pandas系列可以使用以下构造函数创建
# pandas.Series( data, index, dtype, copy)

# data: 数据采取各种形式，如：ndarray(Numpy), list, constants
# index: 索引值必须是唯一的和散列的,与数据的长度相同(默认np.arange(n)如果没有索引被传递)。
# dtype: dtype用于数据类型(如果没有,将推断数据类型)。
# copy: 复制数据,默认为false。

# 1.1.1 创建一个空的系列
s = pd.Series()
# print(s)

# 1.1.2 从ndarray创建一个系列
# 如果数据是ndarray，则传递的索引必须具有相同的长度。 如果没有传递索引值，那么默认的索引将是范围(n)，其中n是数组长度。
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
# print(s)
# 这里没有传递任何索引，因此默认情况下，它分配了从0到len(data)-1的索引，即：0到3

s = pd.Series(data, index=[100, 101, 102, 103])
# print(s)
# 在这里传递了索引值。现在可以在输出中看到自定义的索引值。


# 1.1.3 从字典创建一个系列
# 字典(dict)可以作为输入传递，如果没有指定索引，则按排序顺序取得字典键以构造索引。
# 如果传递了索引，索引中与标签对应的数据中的值将被拉出。
data = {
    'a': 0,
    'b': 1,
    'c': 2
    }
s = pd.Series(data)
# print(s)









