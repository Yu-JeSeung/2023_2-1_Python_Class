import random
com = random.randrange(1,21)
while True:
    user = int(input('1~20 사이의 수 입력: '))
    if com == user:
        break;
    else:
        