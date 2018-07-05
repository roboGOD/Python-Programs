def binCon(n):
    if n == 1:
        return "1"
    elif n == 0:
        return "0"
    return ""+binCon(int(n/2))+str(n%2)

if __name__ == '__main__':
    n = int(raw_input())
    maxCount = 0
    currentCount = 0
    s = binCon(n)
    for j,i in enumerate(s):
        if i == '1':
            currentCount += 1
        else:
            if currentCount > maxCount:
                maxCount = currentCount
            currentCount = 0
        if len(s)-1 == j:
            if currentCount > maxCount:
                maxCount = currentCount
    print maxCount
    print s