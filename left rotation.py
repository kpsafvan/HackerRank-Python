#!/bin/python3

import math
import kos
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])
    a=[]
    a =input().split()
    #print(a)
    
    for i in range(0,d) :
    	temp=a[0]
    	for k in range(1,n):
    		a[k-1]=a[k]
    	a[n-1]=temp	
    print(*a,sep=' ')		
    	
    	