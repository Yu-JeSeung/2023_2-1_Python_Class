import random

ex_list=[]
for i in range(20):
    ex_list.append(random.randrange(0,100))

ex_list.sort()

k=int(input('몇번째 데이터를 원하세요? >> '))

print('')
print('1번 값 중복 허용')
print(ex_list[k-1])
print(ex_list)

print('')
print('2번 값 중복 없이')
count = 1
ex_list2=[]
while(count<=20):
    num=random.randrange(0,51)
    if num not in ex_list2:
        ex_list2.append(num)
        count+=1
ex_list2.sort()
print(ex_list2)

for d in range(k):
    mvalue = min(ex_list2)
    di = ex_list2.index(mvalue)
    del(ex_list2[di])

print(k,'th value',mvalue)