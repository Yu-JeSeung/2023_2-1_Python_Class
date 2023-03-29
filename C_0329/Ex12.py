num1,num2 = map(int,input().split())

nlist = list(map(int,input().split()))
result = []

for k in range(num2):
    sum=0
    i,j=map(int,input().split())
    for k in range(i-1,j):
        sum+=nlist[k]
    result.append(sum)

for k in range(num2):
    print(result[k])