import random

com = random.randrange(3)
gnum=0

while(True):
    user = int(input('가위0 바위1 보2 선택: '))
    print('user = %d, com = %d'%(user,com))
    if(user not in [0,1,2]):
        print('0~2의 값을 입력하세요')
        break
    elif(com==user):
        print('비겼습니다')
    elif(user==0 and com==2) or (user==1 and com==0) or (user==2 and com==1):
        print('당신의 승리')
    else:
        print('컴퓨터의 승리')
    gnum=gnum+1

print('게임의 횟수는 : %d'%gnum)
