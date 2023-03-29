import random as r
import time as t

slot=[0]*3
n = int(input('반복할 횟수 입력 >> '))

while n>0:
    for k in range(3):
        slot[k]=r.randrange(7,10)
        print('%d '%slot[k],end='')
        t.sleep(1)

    if slot[0]+slot[1]+slot(2)==21:
        print('잭팟이 터졌네요')
        break
    else:
        print('아쉽네요~~')
    n-=1
