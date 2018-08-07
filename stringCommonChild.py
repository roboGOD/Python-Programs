def commonChild(s1, s2):
    ### Much Better Solution... Go to Wikipedia Largest Common Subsequence
    ### PyPy is much faster than Python because of JIT Compiler
    n = len(s1)
    c = [[0 for _ in range(n+1)] for __ in range(n+1)]
    
    for i in range(n):
        for j in range(n):
            if s1[i] == s2[j]:
                c[i+1][j+1] = c[i][j] + 1
            else:
                c[i+1][j+1] = max(c[i][j+1], c[i+1][j])
    
    return c[n][n]

### Here's my recursive solution which doesn't work (a lot of bugs!)
'''
godsDict = {}    
def commonChild(s1, s2):
    if s1 == "" or s2 == "":
        return 0
    
    t = (s1, s2)
    if t in godsDict:
        return godsDict[t]
    
    localCount = 0
    i,j = 0,0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
            localCount += 1
        else:
            break
    
    m1 = commonChild(s1[i+1:], s2[j:])
    m2 = commonChild(s1[i:], s2[j+1:])
    
    if m1 > m2:
        godsDict[(s1[i:], s2[j:])] = m1
        return localCount + m1
    else:
        godsDict[(s1[i:], s2[j:])] = m2
        return localCount + m2
'''
    
    

if __name__ == '__main__':
    s1 = raw_input()

    s2 = raw_input()

    result = commonChild(s1, s2)
    print result