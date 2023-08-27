def score(n,alice,g) :
    s=len(n)
    temp=[s]
    temp=[0]*s
    e=0
    for i in range(0,s) :
        #print(n[i])
        if n[i] == '1' :
            temp[i]=temp[i]+1
            t=0
            for k in range(i+1,s)  :
                if(n[k] == '1') :
                    temp[i]=temp[i]+1
                else :
                    break
    d=0
    for i in range(0,s) :
        if temp[i]>d :
            d=temp[i]
            f=i
    n=n[:f]+n[f+d:]
    if g%2 ==0 :
        alice=alice+d
    g=g+1
    w=0
    for l in range(0,len(n)) :
        if n[l]=='1' :
            e=score(n,alice,g)
        else :
            w=w+1
        print(alice)
    if w == len(n) :
        if alice>e :
            return alice;
        else :
            return e;
n=input()
alice =0
g=int(0)
r=score(n,alice,g)
print(r,'asdsa')
