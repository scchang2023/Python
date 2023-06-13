#用 def 定義函式
def do_nothing():
    pass

#用小括號呼叫函式
do_nothing()

def make_a_sound():
    print('quack')
make_a_sound()

def agree():
    return True
if agree():
    print('Splendid!')
else:
    print('Thats was unexpected')

#引數與參數
def echo(anything):
    return anything+' '+ anything
print(echo('Rumplesticltskin'))

def commentary(color):
    if color == 'red':
        return 'It is tomato.'
    elif color == 'green':
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color "+color+"."
comment = commentary('blue')
print(comment)

#如果函式沒有明確地呼叫return，呼叫方會得到None
print(do_nothing())

#位置性引數
def menu(wine, entree, dessert):
    return{'wine':wine, 'entree':entree, 'dessert':dessert}
print(menu('chardonnary', 'chicken', 'cake'))

#關鍵字引數
print(menu(entree = 'beef', dessert='bagel', wine = 'bordeaux'))

#指字預設參數值
def menu(wine, entree, dessert='pudding'):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}
print(menu('chardonnary','chicken'))
#當你提供引數時，函式就會使用它，而不是預設值
print(menu('dunnkelfelder','duck', 'doughnut'))

def buggy(arg, result=[]):
    result.append(arg)
    print(result)
#第1次呼叫是空的
buggy('a')
#第2次呼叫多一個
buggy('b')

#可以這樣寫
def works(arg):
    result=[]
    result.append(arg)
    return result
print(works('a'))
print(works('b'))

#修正的做法是傳入別的東西來代表第一次呼叫
def nonbuggy(arg, result=None):
    if result is None:
        result=[]
    result.append(arg)
    print(result)
nonbuggy('a')
nonbuggy('b')

#用 * 來炸開 / 收集位置引數
# args是個參數tuple，它是以傳給 print_args() 函式的零個以上引數產生的
def print_args(*args):
    print('Positional tuple:', args)
print_args()
print_args(3,2,1,'wait','mm...')

#用 ** 來炸開 / 收集關鍵字引數
def print_kwargs(**kwargs):
    print('keyword arguments:', kwargs)
print_kwargs()
print_kwargs(wine='merlot', entree='mutton', dessert ='macaroon')

#純關鍵字引數
#在函式定義式裡面的 * 代表接下來的start與end必須用具名引數來提供
def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)
data=['a','b','c','d','e','f']
print_data(data)
print_data(data, start=4)
print_data(data, end=2)

#可變與不可變引數
#這是不好的作法
outside = ['one', 'fine', 'day']
def mangle(arg):
    arg[1] = 'terrible!'
print(outside)
mangle(outside)
print(outside)

#Docstrings
#你可以在函式內文的開頭加入一個字串來為函式定義加上說明
def echo(anything):
    'echo returns its input argument'
    return anything
help(echo)

#函式是一級公民
def answer():
    print(42)
answer()
def run_something(func):
    func()
run_something(answer)

def add_args(arg1, arg2):
    print(arg1+arg2)
def run_something_with_args(func, arg1, arg2):
    func(arg1,arg2)
run_something_with_args(add_args, 5, 9)

#定義一個測試函式，讓它接收任意數量的引數，並使用 sum() 函式來計算他們的總合並回傳：
def sum_args(*args):
    return sum(args)
def run_with_position_args(func, *args):
    return func(*args)
print(run_with_position_args(sum_args, 1, 2, 3, 4))

#內部函式
#在另一個函式裡面定義一個函式
def outer(a, b):
    def inner(c, d):
        return c+d
    return inner(a, b)
print(outer(4,7))

#在一個函式裡面多次執行複雑的動作，可以使內部函式
def knights(saying):
    def inner(quote):
        return "we are the knights who say: '%s'" % quote
    return inner(saying)
print(knights('Ni!'))

#closure
#inner2()可以直接使用外面得saying參數，不需要用引數來取得
#knigghts2()會回傳inner2函式名稱，而不是呼叫它
def knights2(saying):
    def inner2():
        return "we are the knights who say: '%s'" % saying
    return inner2
a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(type(a))
print(type(b))
print(a())
print(b())

#匿名函式 lambda
def edit_story(words, func):
    for word in words:
        print(func(word))
stairs = ['thud', 'meow', 'thd', 'hiss']
def enliven(word):
    return word.capitalize()+'!'
edit_story(stairs, enliven)
#來寫lambda，因為enliven很短
edit_story(stairs, lambda word: word.capitalize()+'!')

#產生器
def my_range(first=0, last=0, step=1):
    number = first
    while number < last:
        yield number
        number+=step
ranger = my_range(1,5)
print(ranger)
for x in ranger:
    print(x)

#裝飾器 decorator，是一種函式，會接收一個函式，並回傳另一個函式
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword argments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function
#同一個函式可以使用多個裝飾器
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function
@document_it #自動指派裝飾器
@square_it
def add_ints(a, b):
    return a+b
print(add_ints(3, 5))
#手動指派裝飾器
#cooler_add_ints = document_it(add_ints)
#cooler_add_ints(3,5)

    