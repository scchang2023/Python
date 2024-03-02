# 載入 pandas 模組
import pandas as pd
# 篩選練習 - Series
# data = pd.Series([30, 15, 20])
# print(data)
# # condition = [True, False, True]
# condition =data>18
# print(condition)
# filteredData = data[condition]
# print(filteredData)

data = pd.Series(["您好", "Python", "Pandas"])
# condition = [False, True, True]
condition = data.str.contains("P")
filteredData = data[condition]
print(filteredData)

# 篩選練習 - DataFrame