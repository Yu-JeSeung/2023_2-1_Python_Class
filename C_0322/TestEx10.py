for i in range(2,10):
    print('\n%d단 : '%i,end=" ")
    for j in range(1,10):
        if(j==5):continue
        print('%d X %d = %d'%(i,j,i*j),end=" ")
