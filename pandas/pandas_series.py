# 載入 pandas 模組
import pandas as pd

# 資料索引
# data = pd.Series([5, 4, -2, 3, 7], index=["a","b","c","d","e"])
# print(data)

# 觀察資料
# print("資料型態",data.dtype)
# print("資料數量",data.size)
# print("資料索引",data.index)

# 取得資料：根據順序、根據索引
# print(data[2], data[0])
# print(data["e"], data["d"])

# data = pd.Series([5, 4, -2, 3, 7], index=["a","b","c","d","e"])
# 數字運算：基本、統計、順序
# print("最大值", data.max())
# print("總和", data.sum())
# print("標準差", data.std())
# print("中位數", data.median())
# print("最大三位數", data.nlargest(3))

data = pd.Series([])
# 字串運算：