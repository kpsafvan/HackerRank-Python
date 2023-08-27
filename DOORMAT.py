n=int(input())
s=int((n*3)/2)
s=s+1
d=1
f=1
welcome = 1

for i in range(1,n+1) :
    for k in range(1,(3*n)+1) :
        if i == (n+1)/2 :
            if k < s - 3 or k > s + 3:
                print('-',end='')
            else :
                if welcome == 1:
                    print('WELCOME',end='')
                    welcome = 0
        elif k <=(s+d) and k >= (s-d) :
            if not f == 2 :
                print('.',end='')
                f=f+1
            else :
                print('|',end='')
                f=0
        else :
            print('-',end='')
        
    print()
    if i < n/2 :
        d=d+3
    else:
        d=d-3
g=getch()        
    
    
        
