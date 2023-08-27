#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    n=len(s)
    a=list(s)
    a[0]=s[0].upper()
    for i in range(1,n-1) :
        if s[i]==' ' :
            a[i+1]=s[i+1].upper()
            a[i]=s[i]
        if not s[i-1]==' ' :
            a[i]=s[i]
            

    return "" . join(a)        
    #return a        
    

if __name__ == '__main__':
    

    s = input()

    result = solve(s)
    print(result)

   
