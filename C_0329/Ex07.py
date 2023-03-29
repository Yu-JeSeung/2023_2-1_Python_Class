n = int(input('처리할 데이터의 개수를 입력받으세요 >> '))
listex=[]
# sum=0

for k in range(n):
    print('데이터 입력하세요 >> ',end='')
    listex.append(int(input()))
    # sum+=listex[k]

min,max = listex[0],listex[0]

for k in range(n):
    if(min>listex[k]):
        min=listex[k]
    if(max<listex[k]):
        max=listex[k]

# print('리스트 데이터의 합 : %d, 평균 : %.2f'%(sum,sum/n))
# 내장 함수 sum으로 변경
print('리스트 데이터의 합(함수만) : %d, 평균 : %.2f' % (sum(listex),(sum(listex)/len(listex))))
print('최대값 : %d , 최소값 : %d'%(max,min))