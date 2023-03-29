import random

score = 0
for k in range(5):
    correct = False
    tnum = 0
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    while tnum<3 and not correct:
        print('%d + %d = '%(num1,num2),end='')
        ans = int(input())
        if ans==num1+num2:
            print('Correct!!! %d번 만에 맞춤'%(tnum+1))
            correct=True
            score+=(20-tnum*3)
        else:
            print('Try Again ---')
        tnum+=1
    if tnum==3:
        print('정답은 %d 입니다.'%(num1+num2))
print('Score=%d'%score)