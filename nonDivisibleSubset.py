### Given a set of distinct integers, print the size of a maximal subset of S
### where the sum of any 2 numbers in S' is not evenly divisible by k.

### Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    n = len(S)
    #pairs = []
    #dCounts = {}
    kModuloS = {}


    ### Here Is The Best Solution.
    for i,j in enumerate(S):
        moduloJ = j%k
        if moduloJ == 0:
            kModuloS[moduloJ] = 1
        elif moduloJ == k-moduloJ:
            kModuloS[moduloJ] = 1
        elif moduloJ in kModuloS:
            kModuloS[moduloJ] += 1
        elif moduloJ not in kModuloS:
            kModuloS[moduloJ] = 1

    result = 0
    for key in kModuloS:
        #print kModuloS[key]
        larger = None
        if k-key in kModuloS:
            larger = (max(kModuloS[key], kModuloS[k-key]))
            kModuloS[key] = 0
            kModuloS[k-key] = 0
        else:
            larger = kModuloS[key]
            kModuloS[key] = 0
        result += larger

    return result

    ### Here Is A Better Solution. Which still only solved Half of the test cases
    '''
    for i,j in enumerate(S):
        moduloJ = j%k
        if k-moduloJ in kModuloS:
            for _ in kModuloS[k-moduloJ]:
                pairs.append((S[i], S[_]))
                if S[i] in dCounts:
                    dCounts[S[i]] += 1
                else:
                    dCounts[S[i]] = 1
                if S[_] in dCounts:
                    dCounts[S[_]] += 1
                else:
                    dCounts[S[_]] = 1
        elif moduloJ == 0:
            if 0 in kModuloS:
                for _ in kModuloS[0]:
                    pairs.append((S[i],S[_]))
                    if S[i] in dCounts:
                        dCounts[S[i]] += 1
                    else:
                        dCounts[S[i]] = 1
                    if S[_] in dCounts:
                        dCounts[S[_]] += 1
                    else:
                        dCounts[S[_]] = 1
        if moduloJ in kModuloS:
            kModuloS[moduloJ].append(i)
        else:
            kModuloS[moduloJ] = [i]


    '''

    ### Here Is The Brute Force Solution(Able to pass 9/16 Test Cases)
    '''
    for i in range(n):
        for j in range(i+1, n):
            if (S[i]+S[j])%k == 0:
                pairs.append((S[i], S[j]))
                if S[i] in dCounts:
                    dCounts[S[i]] += 1
                else:
                    dCounts[S[i]] = 1
                if S[j] in dCounts:
                    dCounts[S[j]] += 1
                else:
                    dCounts[S[j]] = 1
    '''

    ### Here Is The Common Subpart of All of the above mentioned Partial Solutions.
    '''
    dCount = 0
    while len(pairs) > 0:
        t1 = pairs[0][0]
        t2 = pairs[0][1]
        
        dCount += 1
        pairs.pop(0)
        if len(pairs) <= 0:
        	break
        
        joTemp = None
        if dCounts[t1] >= dCounts[t2]:
        	joTemp = t1
        else:
            joTemp = t2

        j = 0
        while j < len(pairs):
            if joTemp == pairs[j][0] or joTemp == pairs[j][1]:
                dCounts[pairs[j][0]] -= 1
                dCounts[pairs[j][1]] -= 1
                pairs.pop(j)
            else:
                j += 1

    return len(S) - dCount
    '''

n, k = map(int, raw_input().split())
print nonDivisibleSubset(k, map(int, raw_input().split()))