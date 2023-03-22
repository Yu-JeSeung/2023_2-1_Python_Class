select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))

if(select==1):
    sik=input('수식을 입력하세요 : ')
    print("입력한 수식 계산 : %d"%eval(sik))
elif(select==2):
    num1 = int(input('첫 번째 숫자 입력 : '))
    num2 = int(input('두 번째 숫자 입력 : '))
    sum=0
    for i in range(num1,num2+1):
        sum+=i
    print('%d 와 %d 숫자 사이의 합은 : %d'%(num1,num2,sum))
else :
    print('1 또는 2만 입력하세요.')