def wrap(string, max_width) :
    n= len(string)
    for i in range(0,n,max_width) :
        for j in range(i,i+max_width) :
            print(string[j],end='')
            if(j==n-1) :
                break
        print()
string=input()
max_width=int(input())
wrap(string, max_width)
