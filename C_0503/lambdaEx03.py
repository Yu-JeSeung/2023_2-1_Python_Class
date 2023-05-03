import random as r
import time as t

def sadari(st) :         
    s= r.randrange(st)
    return s                

sdr= [0]
sdr= input('사다리 타기 항목 입력: ').split()
for k in range(len(sdr)) :
    hit= sadari(len(sdr))  
    t.sleep(2)             
    print(k, '번은', sdr[hit])
    del(sdr[hit]) 