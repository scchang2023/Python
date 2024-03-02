# 載入numpy套件
import numpy as np
# 多維陣列維度/形狀操作
# 觀察資料形狀
# data = np.ones(10) # [1,1,1,1,1,1,1,1,1,1]
# print(data.shape)
# data = np.array([
#     [3, 1, 5],
#     [1, 2, 3]
# ])
# print(data.shape)

# 資料轉置
# data = np.array([
#     [2, 4, 1],
#     [1, 5, 0]
# ])
# print(data.shape) #(2, 3)
# print(data.T.shape)

# 扁平化資料
# data = np.array([
#     [
#         [2, 1, 3], [1, 2, 3]
#     ],
#     [
#         [0, 2, 1], [8, 9, 10]
#     ]
# ]) #(2, 2, 3)
# new_data = data.ravel()
# print(new_data)
# print(new_data.shape)

# 重塑資料形狀
# data = np.array([
#     [
#         [2, 1, 3], [1, 2, 3]
#     ],
#     [
#         [0, 2, 1], [8, 9, 10]
#     ]
# ]) # 2x2x3=12
# new_data = data.reshape(3,4) # 3x4=12
# print(new_data)

# data = np.zeros(18).reshape(3, 6)
# print(data)

# data = np.arange(9).reshape(3, 3)
# print(data, type(data))
# print(data.T)