import random

com = random.randrange(3)

user = int(input('가위0 바위1 보2 선택: '))
print('user = %d, com = %d'%(user,com))

if(com==user):
    print('비겼습니다')
elif(user==0 and com==2) or (user==1 and com==0) or (user==2 and com==1):
    print('당신의 승리')
else:
    print('컴퓨터의 승리')
