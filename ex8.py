#制作一個名為 e2f 的英文字典，並印出。
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
print(e2f)

#印出walrus的法文單字
print(e2f['walrus'])

#用 e2f 來製作法英字典，稱為 f2e。使用 items 方法。
f2e={}
for e, f in e2f.items():
    f2e[f] = e
print(f2e)

#印出法文單字 chien 的英文
print(f2e['chien'])

#印出 e2f 的英文單字集合
print(set(e2f))

#製作一個多層的字典，稱之為 life。
life = {'animals':{'cats':['Henri', 'Grumpy', 'Lucy'],'octopi':'','emus':''},
        'plants':'',
        'others':''}
print(f'life = {life}')

#印出life最頂層的鍵
for i, j in life.items():
    print(i)

#印出 life['animals']的鍵
for i, j in life['animals'].items():
    print(i)

#印出 life['animals']['cats']的值
print(life['animals']['cats'])

#使用集合生成式和range(10)之內的奇數來製作odd集合
odd_set = {number for number in range(10) if number%2 ==1}
print(odd_set)

#使用字典生成式來製作字典 squares。使用 range(10)來回傳鍵，並各個平方當成它的值
squares = {i:i*i for i in range(10)}
print(squares)
