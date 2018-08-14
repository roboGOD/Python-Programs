### This was my way... Without using counting sort.

'''
from bisect import bisect_left

def binarySearch(a, x):
    i = 0
    j = len(a)-1
    flag = False
    while i <= j:
        if i == j:
            if flag:
                return -1
            flag = True
        
        mid = (i+j)/2
        
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            j = mid-1
        elif a[mid] < x:
            i = mid+1
    
    return -1
            

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    n = (len(expenditure))
    
    trailing = expenditure[:d]
    trailing.sort()
    notify = 0
    index = long(d/2)
    remIn = binarySearch(trailing, expenditure[0])
    
    for i in range(d, n):
        median = trailing[index]
        if expenditure[i] >= 2*median:
            notify += 1

        #print trailing, notify
        
        trailing.pop(remIn)
        
        #insIn = binaryInsert(trailing, expenditure[i])
        insIn = bisect_left(trailing, expenditure[i])
        trailing.insert(insIn, expenditure[i])
        
        remIn = insIn
    
    return notify
'''


### Here's a better way using Counting sort.

def activityNotifications(expenditure, d):
    
    trailingCounts = [0 for _ in range(201)]
    for i in expenditure[:d]:
        trailingCounts[i] += 1
    
    medianIndex = int(d/2)
    dEven = (d%2 == 0)
    if dEven:
        medianIndex -= 1
    
    notify = 0
    
    for i in range(d, len(expenditure)):
        summ = 0
        flag = False
        for item, count in enumerate(trailingCounts):
            summ += count
            diff = summ-medianIndex
            if summ > medianIndex:
                if dEven:
                    if flag:
                        median = (float(median)+float(item))/2.0
                        break
                    else:
                        median = item
                        if diff != 1:
                            break
                        flag = True
                else:
                    median = item
                    break
        
        if expenditure[i] >= 2.0*median:
            notify += 1
        
        trailingCounts[expenditure[i-d]] -= 1
        trailingCounts[expenditure[i]] += 1
        
    return notify


if __name__ == '__main__':
    nd = raw_input().split()

    n = long(nd[0])

    d = long(nd[1])


    str = raw_input().rstrip().split()

    expenditure = map(int, str)

    result = activityNotifications(expenditure, d)

    print result
