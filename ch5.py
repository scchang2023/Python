#用str()來建立
#print(str(98.6))

#用\來轉義
#palindrome = 'A man,\nA plan,\nA canal'
#print(palindrome)

#用+來結合
#print('Release the kraken' + 'No, wait!')

#用 *來重覆
#start = 'Na '*4+'\n'
#middle = 'Hey ' *3+'\n'
#end = 'Goodbye.'
#print(start + start + middle + end)

#用 [] 取得字元
#letters = 'abcdefghijklmnopqrstuvwxyz'
#print(letters[0])
#print(letters[1])
#print(letters[-1])
#print(letters[-2])
#print(letters[25])
#print(letters[5])
#print(letters[100])

#用 slice 取得子字串
#letters = 'abcdefghijklmnopqrstuvwxyz'
#print(letters[:])
#print(letters[20:])
#print(letters[10:])
#print(letters[12:14])
#print(letters[-3:])
#print(letters[18:-3])
#print(letters[::7])

#用len()取得長度
#letters = 'abcdefghijklmnopqrstuvwxyz'
#print(len(letters))
#empty=''
#print(len(empty))

#用split()來拆分
#tasks='get gloves, get mask, give cat vitamins, call ambulance'
#print(tasks.split(','))

#用join()來結合
#crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
#crypto_string = ','.join(crypto_list)
#print(crypto_string)

#用replace()來替換
#setup = 'a duck goes into a bar...'
#print(setup.replace('duck', 'marmoset'))

#用strip()來剝除
#world = "    earth  "
#print(world.strip())

#搜尋與選擇
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''
#取得前面13個字元
print(poem[:13])
#這首詩有幾個字元
print(len(poem))
#它的開頭是不是All
print(poem.startswith('All'))
#它的結尾是不是 That's all, folks!
print(poem.endswith('That\'s all, folks!'))

#找出 the 這個字在詩中第一次出現時的offeset
word = 'the'
print(poem.find(word))
print(poem.index(word))

#找出 the 這個字在詩中最後一次出現時的offeset
word = 'the'
print(poem.rfind(word))
print(poem.rindex(word))

#如果字串不存在
word = 'duck'
print(poem.find(word))
print(poem.rfind(word))

# the 這個字出現過幾次
word = 'the'
print(poem.count(word))

#詩的字元是否只有字母或數字
print(poem.isalnum())

#移除兩端的 "."
setup = 'a duck goes into a bar...'
print(setup.strip('.'))

#將第一個單字的第一個字母改成大寫
setup = 'a duck goes into a bar...'
print(setup.capitalize())

#將所有單字的第一個字母改成大寫
setup = 'a duck goes into a bar...'
print(setup.title())

#將所有字元改成大寫
setup = 'a duck goes into a bar...'
print(setup.upper())

#將所有字元改成小寫
setup = 'a duck goes into a bar...'
print(setup.lower())

#將大小寫對調
setup = 'a duck goes into a bar...'
print(setup.swapcase())

#在30個空格內置中字串
print(setup.center(30))

#在30個空格內靠左對齊
print(setup.ljust(30))

#在30個空格內靠右對齊
print(setup.rjust(30))

#格式化
#舊式 %
actor = 'Richard Gere'
cat = 'Chester'
weight = 28
print("My wife's favorite actor is %s" % actor)
print("Our cat %s weighs %s pounds" % (cat, weight))

#新式:{}與format()
thing = 'woodchuck'
print('{}'.format(thing))

thing = 'woodchuck'
place = 'lake'
print('The {} is in the {}.'.format(thing, place))

#最新式:f-string
thing = 'wereduck'
place = 'werepond'
print(f'The{thing} is in the {place}')