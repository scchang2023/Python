# 載入 pandas 模組
import pandas as pd
# 建立 Series
# data = pd.Series([20, 10, 15])
# 基本 Series 操作
# print(data)
# print(f"Max {data.max()}")
# print(f"Median {data.median()}")
# data = data *2
# print(data)
# data = data==20
# print(data)


# 建立 DataFrame
data = pd.DataFrame({
    "name":["Amy", "John", "Bob"],
    "salary":[30000, 50000, 40000]
})
# DataFrme 基本操作
# print(data)
# 取得特定的欄位
# print(data["name"])
# print(data["salary"])
# 取得特定的列
print(data.iloc[0])
