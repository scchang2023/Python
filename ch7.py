# 用逗號與()來建立

# 建立空tuple
#empty_tuple=()
#print(empty_tuple, type(empty_tuple))

# 在每個元素後面加上逗號，建立tuple
#one_marx='Groucho',
#print(one_marx, type(one_marx))

# 也可以把它們加在括號裡面
#one_marx=('Groucho',)
#print(one_marx, type(one_marx))

# 若沒有加逗號，型態是字串
#one_marx=('Groucho')
#print(one_marx, type(one_marx))

# 若有多個元素，在每個元素後面加上逗號
#marx_tuple=('Groucho', 'Ghico', 'Harpo')
#print(marx_tuple, type(marx_tuple))

# tuple可以一次給多個變數值
#marx_tuple=('Groucho', 'Chico', 'Harpo')
#a, b, c = marx_tuple
#print(a,b,c)

# 使用tuple來對調值，不需要用到暫時性變數
#password = 'swordfish'
#icecream = 'tuffifrutti'
#print(password, icecream)
#password, icecream = icecream, password
#print(password, icecream)

# 用 touple() 來建立
#marx_list = ['Groucho', 'Chico', 'Harpo']
#print(tuple(marx_list))

# 用 + 來結合 tuple
#print(('Groucho',)+('Chico', 'Harpo'))

# 用 * 來重覆項目
#print(('yada',)*3)

# 比較 tuple
#a=(7,2)
#b=(7,2,9)
#print(a==b)

# 用 for 與 in 來迭代
#words = ('fresh','out','of', 'ideas')
#for word in words:
#    print(word)

# 無法修改 tuple
#t1 = ('Fee', 'Fie', 'Foe')
#t2 = ('Flop',)
#print(f"t1 id = {id(t1)}")
#t1+=t2
#print(t1)
#print(f"t1 id = {id(t1)}")


# 用[]來建立
#empty_list = []
#weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
#print(weekdays)

#用 list() 來建立或轉換
#another_empt_list = list()
#print(another_empt_list)

#將一個字串轉成單字元字串組成的串列
#print(list('cat'))

#將tuple轉成串列
#a_tuple = ('ready','fire','aim')
#print(list(a_tuple))

#用split()和字串來建立
#talk_like_a_private_day = '2023/5/3'
#print(talk_like_a_private_day.split('/'))

#用[offset]來取得項目
#marxes = ['Groucho','Chico','Harpo']
#print(marxes[0])

#用slice取得項目
#marxes = ['Groucho','Chico','Harpo']
#print(marxes[0:2])

#從前面開始，以2的間隔值往右取出元素
#marxes = ['Groucho','Chico','Harpo']
#print(marxes[::2])

#就地翻轉
#marxes = ['Groucho','Chico','Harpo']
#marxes.reverse()
#print(marxes)

#用append()將項目加到尾端
#marxes = ['Groucho','Chico','Harpo']
#marxes.append('Zeppo')
#print(marxes)

#用insert()和offset加入項目
#marxes = ['Groucho','Chico','Harpo']
#marxes.insert(2,'Gummo')
#print(marxes)

#用 * 來重覆所有項目
#print(['blah']*3)

#用 extend() 結合串列
#marxes = ['Groucho','Chico','Harpo']
#others = ['Gummo', 'Karl']
#marxes.extend(others)
#print(marxes)

#用 + 來結合串列
#marxes = ['Groucho','Chico','Harpo', 'Zeppo']
#others = ['Gummo', 'Karl']
#marxes += others
#print(marxes)

#用 offset 來更改一個項目
#marxes = ['Groucho','Chico','Harpo']
#marxes[2] = 'Wanda'
#print(marxes)

#用 slice 改變項目
#numbers = [1, 2, 3, 4]
#numbers[1:3] = [8, 9]
#print(numbers)
#numbers = [1,2,3,4]
#numbers[1:3]=(98,99,100)
#print(numbers)

#用 del 和 offset 來刪除一個項目
#marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
#print(marxes[-1])
#del marxes[-1]
#print(marxes)

#用 remove() 與值來刪除項目
#marxes = ['Groucho', 'Chico', 'Harpo']
#marxes.remove('Groucho')
#print(marxes)

#用 pop() 和 offset 取出項目並刪除它
#marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
#print(marxes.pop())
#print(marxes)
#marxes.pop(1)
#print(marxes)

#用clear()刪除所有項目
#work_quotes = ['Working hard?', 'Qick question!', 'Number one priorities!']
#print(work_quotes)
#work_quotes.clear()
#print(work_quotes)

#用index()和值來找到項目的offset
#marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
#print(marxes.index('Chico'))
#simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
#print(simpsons.index('Bart'))

#用in來檢查值是否存在
#marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
#print('Groucho' in marxes)
#print('Bob' in marxes)

#同一個值可能出現在串列的多個位置，只要出現一次，in就會回傳True
#words = ['a', 'deer', 'a', 'female', 'deer']
#print('deer' in words)

#用count()來計算一個值的出現次數
#marxes = ['Groucho', 'Chico', 'Harpo']
#print(marxes.count('Harpo'))
#print(marxes.count('Bob'))

#用join()將串列轉成字串
#marxes = ['Groucho', 'Chico', 'Harpo']
#print(', '.join(marxes))

#用sort()或sorted()來排序項目
#串列方法sort()可就地排序串列本身
#通用函式sorted()可回傳排序後的串列複本
#marxes = ['Groucho', 'Chico', 'Harpo']
#sorted_marxes = sorted(marxes)
#print(sorted_marxes)
#marxes.sort()
#print(marxes)

#用len()取得長度
#marxes = ['Groucho', 'Chico', 'Harpo']
#print(len(marxes))

#用= 來賦值
#a = [1,2,3]
#print(a)
#b = a
#print(b)
#a[0] = 'surprise'
#print(a)

#用copy()、list()或slice來複制
#a=[1,2,3]
#b=a.copy()
#c=list(a)
#d=a[:]
#print(a,b,c,d)

#用deepcopy()複制所有的東西
#a=[1,2,[8,9]]
#b=a.copy()
#c=list(a)
#d=a[:]
#print(a,b,c,d)
#a[2][1] = 10
#print(a,b,c,d)

#import copy
#a=[1,2,[8,9]]
#b=copy.deepcopy(a)
#print(a,b)
#a[2][1]=10
#print(a,b)

#比較串列
#a=[7,2]
#b=[7,2,9]
#print(a==b)
#print(a<=b)

#用for與in來迭代
#cheeses = ['brie', 'gjetost', 'havarti']
#for cheese in cheeses:
#    print(cheese)

