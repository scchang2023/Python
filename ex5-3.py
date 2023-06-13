# 用舊式格式化寫出下面的詩。將字串'roast beef'、'harm'、'head'與'clam'代入這個字串
poem= """
    My kitty cat likes %s,
    My kitty cat likes %s,
    My kitty cat fell on his %s
    And now thins he's a %s
"""
args = ('roast beef', 'harm', 'head', 'clam')
print(poem % args)
