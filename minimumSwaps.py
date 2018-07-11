### Sometimes the problem is really simple and easy and we ourselves make it too complex.


def minimumSwaps(arr):
    '''
    prevSwapIn = None
    def cost(i1, i2):
        minCost = None
        minIndex = None
        for i in range(i1,i2+1):
            if i == prevSwapIn:
                continue
            tempCost = abs(arr[i1-1] - 1 - i) + abs(arr[i] - i1)
            if minCost == None:
                minCost = tempCost
                minIndex = i
            elif minCost > tempCost:
                minCost = tempCost
                minIndex = i
        return minIndex
    '''        
    swaps = 0
    id1 = 0
    while id1 < len(arr)-1:
        id2 = arr[id1]-1
        if id1 == id2:
            id1 += 1
            continue
        swapIndex = id2
        swaps += 1
        ### Swap arr[id1] with arr[id2]
        arr[id1], arr[swapIndex] = arr[swapIndex], arr[id1]
        #print id1, "and",swapIndex
        #prevSwapIn = swapIndex
    return swaps
if __name__ == '__main__':

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)
    print res