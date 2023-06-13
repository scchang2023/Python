#字典
#用{}來建立
empty_dict={}
print(empty_dict)

bierce = {"day": "A period of twenty-four hours, mostly misspent",
          "positive": "Mistaken at the top of one's voice",
          "misfortune": "The kind of fortune that never misses"}
print(bierce)

#使用dict()做法
acme_customer = dict(first="while",middle="E", last="Coyote")
print(acme_customer)

#用dict()來轉換
lol = [['a','b'],['c','d'],['e','f']]
print(dict(lol))

lot = [('a','b'),('c','d'),('e','f')]
print(dict(lot))

#用[鍵]來加入或改變一個項目
pythons = {'Chapman':'Graham',
           'Cleese':'John',
           'Idle':'Eric',
           'Jones':'Terry',
           'Palin':'Michael'}
print(pythons)
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'
print(pythons)

#用[key]或get()取得一個項目
some_pythons = {'Graham':'Chapman',
                'John':'Cleese',
                'Eric':'Idle',
                'Terry':'Gilliam',
                'Michael':'Palin',
                'Terry':'Jones'
                }
print(some_pythons)
print(some_pythons['John'])
print(some_pythons.get('John'))
print(some_pythons.get('Groucho','Not a python'))

#用 keys() 取得所有的鍵
signals ={'green':'go',
          'yellow':'go faster',
          'red':'smile for the camera'}
print(list(signals.keys()))

#用values()取得所有的值
print(list(signals.values()))

#用 items() 取得每一對鍵/值
print(list(signals.items()))

#用 len()取得長度
print(len(signals))

#用 {**a, **b} 來結合字典
first = {'a':'agony', 'b':'bliss'}
second = {'b':'bagells', 'c':'candy'}
third = {'d':'donuts'}
print({**first, **second, **third})

#用update()結合字典
pythons = {'Chapman':'Graham',
           'Cleese':'John',
           'Gilliam':'Terry',
           'Idle':'Eric',
           'Jones':'Terry',
           'Palin':'Michael'}
print(pythons)
others = {'Marx':'Groucho', 'Howard':'Moe'}
pythons.update(others)
print(pythons)

#第2個字典的鍵與要合併的字典的鍵一樣時，第2個字典的值會勝出
first = {'a':1, 'b':2}
second = {'b': 'platypus'}
first.update(second)
print(first)

#用del和鍵來刪除項目
del pythons['Marx']
print(pythons)

#用pop()和鍵取得項目並刪除它
#pop()是get()和del的結合
print(len(pythons))
print(pythons.pop('Palin'))
print(len(pythons))

#用clear()刪除所有項目
pythons.clear()
print(pythons)

#用in來檢測鍵
pythons = {'Chapman':'Graham', 'Cleese':'John',
           'Jones':'Terry', 'Palin':'Michael', 'Idle':'Eric'}
print('Chapman' in pythons)
print('Gilliam' in pythons)

#用=來賦值
signals = {'green':'go',
           'yellow':'go faster',
           'red':'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)

#用copy來複制
signals = {'green':'go',
           'yellow':'go faster',
           'red':'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(f"signals = {signals}")
print(f"original_signals = {original_signals}")

#集合(set)就像沒有值，只留下鍵的字典。
#用set()建立，集合是無序的。
empty_set = set()
print(f"empty_set = {empty_set}")
even_numbers = {0,2,4,6,8}
print(f"even_numbers = {even_numbers}")
odd_numbers = {1, 3, 5, 7, 9}
print(f"odd_numbers = {odd_numbers}")

#用set()來轉換
print(set('letters'))

#用串列來製作集合
print(set(['Dasher','Dancer', 'Prancer', 'Mason-Dixon']))
#用tuple來製作集合
print(set(('Dasher','Dancer', 'Prancer', 'Mason-Dixon')))
#當你用字典丟給set()時，它只會使用鍵
print(set({'apple':'red', 'orange':'orange', 'cherry':'red'}))
#用len()取得長度
reindeer = set(['Dasher','Dancer', 'Prancer', 'Mason-Dixon'])
print(len(reindeer))
#用add()加入項目
s = set((1,2,3))
print(s)
s.add(4)
print(s)

#用remove()刪資項目
s = set((1,2,3))
s.remove(3)
print(s)

#用for 與in 迭代
furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)

#用 in 來檢查值是否存在
drinks = {'martini':{'vodka', 'vermouth'},
          'black russian':{'vodka', 'kahlua'},
          'white russian':{'cream', 'kahlua', 'vodka'},
          'manhattan':{'rye', 'vermouth', 'bitters'},
          'screwdriver':{'orange juice', 'vodka'}
        }
#for name, contents in drinks.items():
#    if 'vodka' in contents:
#        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not('vermouth' in contents or 'cream' in contents):
        print(name)

#組合與運算子
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']
#交集
print(bruss&wruss)
#聯集
print(bruss|wruss)
#差集
print(bruss-wruss)
print(wruss-bruss)