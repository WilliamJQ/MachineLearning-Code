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

data = {
    'a': 0,
    'b': 1,
    'c': 2
}

s = pd.Series(data,index=['b', 'a', 'c', 'f'])
# print(s)


# 1.1.4 从标量创建一个系列
s = pd.Series(5,index=['a', 'b', 'c', 'd'])
# print(s)

# 1.1.5 从具有位置的系列中访问数据
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# print(s['a'])


# 使用数字索引创建的系列，如果新的数字索引和默认的[0,1,2,...]不同则会将新的数字索引覆盖默认的数字索引，
# 即不能使用默认数字索引来访问元素。如果新的索引是字符索引，那么除了使用新索引访问还是可以使用默认数字索引来访问元素。
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[100, 101, 102, 103])
# print(s[100])

# 1.1.6 检索系列中的前三个元素。
# 如果a:被插入到其前面，则将从该索引向前的所有项目被提取。
# 如果使用两个参数(使用它们之间)，两个索引之间的项目(不包括停止索引)。
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# print(s[:3])

# 1.1.7 检索最后三个元素
# print(s[-3:])

# 1.1.8 打印所有元素
# print(s[:])


# 1.2 数据帧

# pandas中的DataFrame可以使用以下构造函数创建
# pandas.DataFrame( data, index, columns, dtype, copy)
# 1 data	数据采取各种形式，如:ndarray，series，map，lists，dict，constant和另一个DataFrame。
# 2	index	对于行标签，要用于结果帧的索引是可选缺省值 - np.arrange(n)，如果没有传递索引值。
# 3	columns	对于列标签，可选的默认语法是 - np.arange(n)。 这只有在没有索引传递的情况下才是这样。
# 4	dtype	每列的数据类型。
# 5	copy	如果默认值为False，则此命令(或任何它)用于复制数据。


# Pandas数据帧(DataFrame)可以使用各种输入创建，如
# 列表
# 字典
# 系列
# Numpy ndarrays
# 另一个数据帧(DataFrame)

# 1.2.1 创建一个空的DataFrame
df = pd.DataFrame()
# print(df)

# 从列表创建DataFrame
data = [1, 2, 3, 4, 5, 6]
df = pd.DataFrame(data)
# print(df)


data = [['Alex', 10, 90], ['John', 20, 100], ['Mary', 30, 98]]
df = pd.DataFrame(data, index=['a', 'b', 'c'], columns=['name', 'age', 'grade'], dtype=float)
# print(df)

data = {
    'name': ['Alex', 'John', 'Mary'],
    'Age': [18, 19, 20],
}
df = pd.DataFrame(data)
print(df)













