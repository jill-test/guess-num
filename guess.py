#產生一個隨機數字1~100(不要印)
#讓使用者重複輸入數字去猜
#猜對印出 "終於猜對了!"
#猜錯要告訴他 比答案大/小

import random
r = random.randint(1, 100)
#print(r)
while True:
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('你猜中了!')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
