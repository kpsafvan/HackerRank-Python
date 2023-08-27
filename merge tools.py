def merge_the_tools(string, k):

    # your code goes here
    n=len(string)
    a=list(string)
    #a[2]=a[3]
    #print("".join(a))
    m=(n//k) + 1 
    s=[['']*m]*k
    for i in range(0,n,k) :
        for j in range(i,i+k) :
            s[i][j]=a[j]
    print(s)        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
