def merge_the_tools(string, k):

    # your code goes here
    n=len(string)
    a=list
    b=list
    for i in range(0,n,k) :
        a=string[i:i+k]
        #b=[ ele for ele in  if ele % 2 ==0]
        #b=[ele for ele in a if ele not in b]
        seen = set()
        a= [x for x in a if not (x in seen or seen.add(x))]
        print("".join(a))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
