# rabbit = [1,1]

# def sum(x,y):
#     return x+y

# for i in range(11):
#     rabbit.append(sum(rabbit[i],rabbit[i+1]))

# print(rabbit)

def fibo(n):
    if n<2:return 1
    else: return fibo(n-1)+fibo(n-2)

for k in range(13):
    print('%d 개월 후 토끼의 수 = %d' %(k,fibo(k)))
