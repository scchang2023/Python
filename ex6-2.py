# 將值 7 指派給變數 guess_me，並將值 1 指派給變數 number。寫一個 while 迴圈來比較 number 與 guess_me。
# 如果 number 小於 guess_me，印出 too low。如果 number 等於 guess_me，印出 found it 並離開迴圈。
# 如果 number 大於 guess_me，印出 oops 並離開迴圈。在迴圈結束時遞增數字。
guess_me=7
number=1
while True:
    if number<guess_me:
        print(f"{number} too low")
    elif number==guess_me:
        print(f"{number} found it!")
    else:
        print(f"{number} oops")
        break
    number+=1