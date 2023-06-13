#用while來重覆執行
count = 1
while count<=5:
    print(count)
    count+=1

#用else來檢查break
numbers = [1, 3, 5]
position = 0
while position<len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position+=1
else:
    print('No even number found')

#用 for 與 in 來迭代
word = 'thud'
offset = 0
while offset< len(word):
    print(word[offset])
    offset+=1
for letter in word:
    print(letter)

#用break來取消
word = 'thud'
for letter in word:
    if(letter=='u'):
        break
    print(letter)

#用range()來產生數序列
for x in range(0,3):
    print(x)

print(list(range(0,3)))

