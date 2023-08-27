n=int(input())
for i in range(0,n+1) :
    for k in range(1,2*i) :
            if(k<=i) :
                print(k,end='')
            else :
                print(((2*i)-k),end='')
    print()           
