n = int(input('처리할 데이터의 개수를 입력받으세요 >> '))
listex=[]
sum=0

for k in range(n):
    print('데이터 입력하세요 >> ',end='')
    listex.append(int(input()))
    sum+=listex[k]

print('리스트 데이터의 합 : %d, 평균 : %.2f\n'%(sum,sum/n))