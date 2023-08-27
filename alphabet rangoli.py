import string
def print_rangoli(size):
    d=0
    f=size-1
    s=list
    for i in range(0,(2*size)-1):
        for j in range(0,(4*size)-3) :
            s=list(ele for ele in range((((4*size)-3)//2)-d,((((4*size)-3)//2)+d)+1,2))
            if j in s : 
                print(string.ascii_lowercase[f],end='')
                if j < ((4*size)-3)//2 :
                    f=f-1
                else :
                    f=f+1
            else :
                print('-',end='')
        print()
        print(s)
        if i < ((2*size)-1)//2 :
            d=d+2
        else :
            d=d-2
        s=[]
        f=size-1
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    y=input()