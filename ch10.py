#用class定義類別
class Cat():
    def __init__(self, name):
        self.name = name
#用類別來建立物件
#a_cat = Cat()
#another_cat = Cat()
#print(a_cat)

#將屬性指派給第一個物件
#a_cat.age = 3
#a_cat.name = "Mr. FuzzyButtons"
#a_cat.nemesis = another_cat
#print(a_cat.age, a_cat.name, a_cat.nemesis)

#方法
#初始化
# __init__()是特殊的python方法名稱，它的功能是在類別定義式初始化個別的物件
# self 引數則代表它引用個別物件本身
# 傳遞一個字串給name參數
#futball = Cat('Grumpy')

# 繼誠
#class Car():
#    pass
#class Yugo(Car):
#    pass
#用 issubcalss()查看一個類別是否衍生自另一個類別
#print(issubclass(Yugo, Car))
#建立物件
#give_me_a_car = Car()
#give_me_a_yugo = Yugo()

#class Car():
#    def exclaim(self):
#        print("I'm a car!")
#class Yugo(Car):
#    pass
#give_me_a_car = Car()
#give_me_a_yugo = Yugo()
#give_me_a_car.exclaim()
#give_me_a_yugo.exclaim()

#覆寫方法
class Car():
    def exclaim(self):
        print("I'm a car!")
class Yugo(Car):
    def exclaim(self):
        print("I'm a yougo! Much like a Car, but more Yugo-ish.")
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()