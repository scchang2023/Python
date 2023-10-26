# 載入 pandas 模組
import pandas as pd
# 資料索引
data = pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000, 50000, 40000]
}, index = ["a","b", "c"])
print(data)