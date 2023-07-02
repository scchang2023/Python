# 用 if 來選擇
## 用 # 來註釋
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
#檢查 disaster的值，印出相對應的評語
disaster = True #糟糕
if disaster:
    print("Woe!")
else:
    print("Whee!")
```
``` python
Woe!
```
``` python
#在測試式裡面使用測試式，層數依你的需求定：
furry = True
large = True
if furry:
    if large:
        print("It's a yeti")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a whale")
    else:
        print("It's a human!")    
```
``` python
It's a yeti
```
``` python
# 測試可能性超過2個，可以用 if、elif、else。
color = 'mauve'
if color == 'red':
    print("It's a tomato")
elif color == 'green':
    print("It's a green pepper")
elif color == 'bee purple':
    print("I don't know what it is.")
else:
    print("I've never heard of the color", color)
```
``` python
I've never heard of the color mauve
```
python 的比較運算子
```
相等        ==
不相等      !=
小於        <
小於等於    <=
大於        >
大於等於    >=
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
