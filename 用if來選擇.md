# 用 if 來選擇
## 用 \ 來延續一行文字
``` python
sum = 1 + \
2 + \
3 + \
4
sum
```
``` python
10
```
## 用 if、elif、與 else 來進行比較
``` python
disaster = True #糟糕
if disaster:
    print("Woe!")
else:
    print("Whee!")
```
``` python
Woe!
```
## 什麼是 True
- false 值不一定是明確的布林 False。這些被視為 False，其它則視為 True。
    - 布林 False
    - null None
    - 整數零 0
    - 浮點數零 0.0
    - 空字串 ''
    - 空串列 []
    - 空 tuple ()
    - 空字典 {}
    - 空集合 set()
