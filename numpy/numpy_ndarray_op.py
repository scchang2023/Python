import numpy as np

# 逐元運算 (elementwise)
# data1 = np.array([3, 2, 10])
# data2 = np.array([1, 3, 6])
# result = data1+data2
# print("加法 ", result)
# result = data1*data2
# print("乘法 ", result)
# result = data1>data2
# print("大於 ", result)
# result = data1 == data2
# print("等於 ", result)

# 矩陣運算 (matrix)
# data1 = np.array([
#     [1, 3]
# ]) # 1x2
# data2 = np.array([
#     [2, -1, 3],
#     [-2, 4, 1]
# ]
# ) # 2x3
# result = data1@data2 # result = data1.dot(data2)
# print("內積", result)
# result = np.outer(data1, data2)
# print("外積", result)

# 統計運算 (statistics)
# ndarray 多維陣列 簡稱陣列
data = np.array([
    [2, 1, 7],
    [-5, 3, 8]
]) # 2x3
# result = data.sum()
# print("總和", result)
# result = data.max()
# print("最大值", result)
# result = data.mean()
# print("平均值", result)
# result = data.std()
# print("標準差", result)

# result = data.sum(axis=0) # 針對欄做總合 column (針對第一個維度做總合)
# print(result)
# result = data.sum(axis=1) # 針對列做總合 row (針對第二個維度做總合)
# print(result)
# result = data.max(axis=0)
# print(result)
# result = data.mean(axis=1)
# print(result)

result = data.cumsum() #逐元累加
print(result)