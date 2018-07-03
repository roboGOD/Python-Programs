#!/bin/python

import math
import os
import random
import re
import sys
from time import time




# Complete the morganAndString function below.
def morganAndString(a, b):
    s = []
    a = a + 'z'
    b = b + 'z'
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            s.append(a[i])
            i += 1
        elif a[i] > b[j]:
            s.append(b[j])
            j += 1
        else:
            if a[i:] <= b[j:]:
                s.append(a[i])
                i += 1
            else:
                s.append(b[j])
                j += 1
    result = ''.join(s)            
    return result[:(len(result)-1)]
        	'''
            t1 = i
            t2 = j
            cVal1 = None
            cVal2 = None
            while t1 < len(a) and t2 < len(b) and a[t1] == b[t2]:
                if cVal1 == None:
                    cVal1 = t1
                    cVal2 = t2
                    s.append(a[cVal1])
                    cVal1 += 1
                elif a[cVal1:] <= b[cVal2:]:
                    s.append(a[cVal1])
                    cVal1 += 1
                elif a[cVal1:] > b[cVal2:]:
                    s.append(b[cVal2])
                    cVal2 += 1
                t1 += 1
                t2 += 1

            if t1 < len(a) and t2 < len(b):
                if a[t1] < b[t2]:
                    i = cVal1
                    j = cVal2
                elif a[t1] > b[t2]:
                    temp = j
                    j = j + cVal1 - i
                    i = i + cVal2 - temp

            elif t1 < len(a):
                i = cVal1
                j = cVal2
                if i < (len(a)-1) and a[i] > a[i+1] and j >= len(b) and a[cVal1] == b[cVal2-1]:
                    i = i + 1
                    j = j - 1
            else:
                i = cVal1
                j = cVal2
                if j < (len(b)-1) and b[j] > b[j+1] and i >= len(a) and a[cVal1-1] == b[cVal2]:
                    i = i - 1
                    j = j + 1
            
    
    while i < len(a):
        s.append(a[i])
        i += 1
    
    while j < len(b):
        s.append(b[j])
        j += 1
        
    result = ''.join(s)
    return result
    '''
            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    rl = []
    t = int(raw_input())
    for t_itr in xrange(t):
        a = raw_input()

        b = raw_input()
        ss1 = time()
        result = morganAndString(a, b)
        ss2 = time()

        #fptr.write(result + '\n')
        rl.append(result)

    #fptr.close()
    for i in rl:
        print i

    print "Time Taken is:: ", round(ss2 - ss1, 8)
