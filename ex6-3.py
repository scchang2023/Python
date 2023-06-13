# 將值 5 指派給變數 guess_me。使用 for 迴圈在 range(10)之內迭代一個名為 number 的變數。
# 如果 number 小於 guess_me，印出 too low。如果它等於 guess_me，印出 found it!，接著跳
# 出迴圈。如果 number 大於 guess_me，印出 oops 並離開迴圈。
guess_me=5
for number in range(1,10):
    if number<guess_me:
        print(f"{number} too low")
    elif number==guess_me:
        print(f"{number} found it")
    else:
        print(f"{number} oops")
        break