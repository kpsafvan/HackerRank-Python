from sys import stdin, stdout
n = int(input())
s=[]
d=''
for i in range(0,n) :
    a=str(input())
    s.append(a)
print(len(set(s)))    
for i in range(0,n) :
    f=1
    if  s[i] != '' :
        for k in range(n-1,-1,-1) :
                if k !=i and s[k] == s[i] :
                    f=f+1
                    s[k] =''
        #print(f,end=' ')            
        d=d+' ' +str(f)
        #d.append(' ')
        s[i]=''               
stdout.write(str(d))
#print(*d)        
 
                
