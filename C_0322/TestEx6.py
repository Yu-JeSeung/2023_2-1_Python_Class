num = int(input('정수를 입력하세요 : '))
sum=0
sum2=0

for i in range(0,num+1,2):
    sum+=i

i=0
while i <= num:
    if(i%2==0):
        sum2+=i
    i=i+1


print('for문 : 입력받은 정수까지 짝수의 합은 : %d'%sum)
print('while문 : 입력받은 정수까지 짝수의 합은 : %d'%sum2)