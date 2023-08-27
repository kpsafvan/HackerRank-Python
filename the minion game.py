def minion_game(a):
    # your code goes here
    n = len(a)
    stuart=0
    kevin=0
    vowels = ['A','E','I','O','U']
    for i in range(0,n) :
        if a[i] in vowels :
            kevin = kevin + ((n-i))
        else :
            stuart =stuart + ((n-i))
    print(kevin,'   ',stuart)
    if(kevin < stuart) :
        print('Stuart ',stuart,sep='')
    elif(stuart < kevin):
        print('Kevin ',kevin,sep='')
    else :
        print('Draw')
            



if __name__ == '__main__':
    s = input()
    minion_game(s)
