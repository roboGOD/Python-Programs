### Again... A rather simpler solution with really cool logic. Thinking just not out of the box, but out of the Dimension.
### How do you come up with that?

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    for tuples in queries:
        arr[tuples[0]-1] += tuples[2]
        arr[tuples[1]] -= tuples[2]
    mx = 0
    summ = 0
    for i in arr:
        summ += i
        mx = max([mx,summ])
    return mx

'''

def arrayManipulation(n, queries):
    """
    ls = [0]*n
    for i in queries:
        for j in range(i[0]-1,i[1]):
            ls[j] += i[2]
    return max(ls)
    """
    d = {}
    def addTuples(t1,t2,t3):
        if t1 == t2:
            return
        flag = True
        for tuples in d.keys():
            if t1 >= tuples[0] and t1 <= tuples[1]:
                flag = False
                val = d[tuples]
                d.pop(tuples)
                d[(tuples[0],t1-1)] = val
                if t2 >= tuples[1]:
                    d[(t1,tuples[1])] = val + t3
                    addTuples(tuples[1]+1,t2,t3)
                else:
                    d[(t1,t2)] = val + t3
                    d[(t2+1, tuples[1])] = val
            elif t1 >= tuples[0] and t1 >= tuples[1]:
                pass
            elif t2 >= tuples[0] and t2 <= tuples[1]:
                flag = False
                val = d[tuples]
                d.pop(tuples)
                addTuples(t1,tuples[0]-1,t3)
                d[(tuples[0],t2)] = val + t3
                d[(t2+1, tuples[1])] = val
            elif t2 >= tuples[0] and t2 >= tuples[1]:
                flag = False
                val = d[tuples]
                #d.pop(tuples)
                addTuples(t1,tuples[0]-1,t3)
                d[(tuples[0],tuples[1])] = val + t3
                addTuples(tuples[1]+1,t2,t3)
        if flag:
            d[(t1,t2)] = t3
            
    
    for i in queries:
        t1,t2 = i[0],i[1]
        if (t1,t2) in d:
            d[(t1,t2)] += i[2]
        else:
            addTuples(t1,t2,i[2])
    for k,v in d.items():
        print k,v
    return max(d.values())            

'''

if __name__ == '__main__':

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    print result
