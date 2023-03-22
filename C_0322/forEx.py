sum = 0

for i in range(2,31,2):
    print(i, end=" ")
    sum+=i
print('\n%d'%sum)

mul = 1
for k in range(9,0,-1):
    print(k,end=" ")
    mul*=k
print('\n곱한 값은 = %d'%mul)