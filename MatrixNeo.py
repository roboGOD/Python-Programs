
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    matrix = []
    dec = []
    for i in range(m):
        dec.append("")
    
    for _ in xrange(n):
        matrix_item = raw_input()
        matrix.append(matrix_item)
        for j in range(m):
            dec[j] += matrix_item[j]
    
    dMsg = ""
    for i in dec:
        dMsg += i
        #print i
        
    fMsg = re.sub(r'([\w])[\W]+([\w])', r'\1 \2', dMsg)
    print fMsg

