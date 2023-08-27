n,m = input().split(' ')
n = float(n)
m=int(m)
array=[]
a=[]
s=[]
array = input().split(' ')
a = input().split(' ')
s = input().split(' ')
print(array)
print(a)
print(s)

h = 0
for i in range(0,m) :
    if a[i] in array :
        h = h+ 1
    if s[i] in array :
        h= h-1
print(h)        
    

