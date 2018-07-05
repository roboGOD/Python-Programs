# Any Intelligent Fool can make it bigger and more comlex.
# It takes a touch of a genius to make it simple.

# Complete the almostSorted function below.
''' 
### Baaka! It's really hard to do it without sorting.
def almostSorted(a):
    ls = []
    revCheck = False
    rev = False
    reverse = False
    swap1 = False
    swap2 = False
    waiting = False
    grandpa = None
    parent = None
    i = 0
    while i < len(a):
    	baby = a[i]
        
        if parent == None:
            parent = i
        
        elif grandpa == None:
            if a[parent] > baby:
                ls.append(i)
                revCheck = True
            grandpa = parent
            parent = i

        elif a[parent] < baby and not revCheck and not rev:
            grandpa = parent
            parent = i

        elif a[parent] > baby and not revCheck and not rev:
            if swap1 == True or reverse == True:
                print "no"
                return
            ls.append(i)
            revCheck = True
            parent = i
        
        elif a[parent] > baby and revCheck:
            if swap1 == True or reverse == True:
                print "no"
                return
            rev = True
            revCheck = False
            if a[grandpa] > baby:
                if grandpa != 0:
                    print "no"
                    return
                else:
                    pass
            parent = i
        
        elif a[parent] < baby and revCheck:
            if swap2 == True or reverse == True:
                print "no"
                return
            if a[parent-1] > baby:
            	if swap1 == True and waiting == False:
                	waiting = True
                	revCheck = False
                	grandpa = parent
                	parent = i
                elif swap1 == True and waiting == True:
                	waiting = False
                	swap2 = True
            else:
            	revCheck = False
            	swap1 = True
            	### Swapping
            	tempSwap = a[parent-1] 
            	a[parent-1] = a[parent]
            	a[parent] = tempSwap
            
            	if parent - 2 <= 0:
            		i =0
            		parent= None
            		grandpa = None
            	elif parent - 2 == 1:
            		i = 1
            		grandpa = None
            		parent = 0
            	else:
            		i = parent - 2
            		parent = i-1
            		grandpa = i-2
            	continue


        elif a[parent] > baby and rev:
            if a[grandpa] > baby:
                if grandpa != 0:
                    print "no"
                    return
                else:
                    pass
            parent = i

        elif a[parent] < baby and rev:
            if a[grandpa] > baby:
                print "no"
                return
            if swap1 == True or reverse == True:
                print "no"
                return    
            reverse = True
            rev = False
            parent = i
            ls.append(i)
            if grandpa != 0:
                grandpa += 1
        
        if i == len(a)-1:
        	if waiting == True:

            if revCheck:
                if swap1 == True or reverse == True:
                    print "no"
                    return
                if a[parent-2] > baby and len(a) > 2:
                    print "no"
                    return
                swap1 = True
                ### Swapping
            	tempSwap = a[parent-1] 
            	a[parent-1] = a[parent]
            	a[parent] = tempSwap
            
            	if parent - 2 <= 0:
            		i =0
            		parent= None
            		grandpa = None
            	elif parent - 2 == 1:
            		i = 1
            		grandpa = None
            		parent = 0
            	else:
            		i = parent - 2
            		parent = i-1
            		grandpa = i-2
            	continue
            elif rev:
                if a[grandpa] > baby:
                    print "no"
                    return
                if swap1 == True or reverse == True:
                    print "no"
                    return    
                reverse = True
                ls.append(i)
        i += 1                

    print "yes"
    if swap1 :
        print "swap", ls[0], ls[0]+1
    elif reverse:
        print "reverse", ls[0], ls[1]

'''

def checkAlmostSotrted(nums):
    # test whether nums[lo:hi+1] is sorted or not
    def isSorted(nums, lo, hi):
        i = lo + 1
        while i <= hi:
            if nums[i] < nums[i - 1]:
                return False
            i += 1
        return True

    def exch(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    if isSorted(nums, 0, len(nums) - 1):
        print "yes"
    else:
        sortedNums = nums[:]
        sortedNums.sort()

        # find the leftmost index which nums[idx] != sortedNums[idx]
        lIdx = 0
        while lIdx < len(nums) and nums[lIdx] == sortedNums[lIdx]:
            lIdx += 1

        # find the rightmost index
        rIdx = len(nums) - 1
        while rIdx >= 0 and nums[rIdx] == sortedNums[rIdx]:
            rIdx -= 1
        # nums is not sorted, so there are at least 2 indexes out of place.

        # test if we can just swap to get sorted nums
        exch(lIdx, rIdx)
        if isSorted(nums, lIdx, rIdx):
            print "yes"
            print "swap %d %d" % (lIdx + 1, rIdx + 1)
        else:
            # test if we can reverse the segments to get a sorted array
            exch(lIdx, rIdx) # swap back
            seg = nums[lIdx:rIdx+1]
            seg.reverse()
            if isSorted(seg, 0, len(seg)- 1):
                print "yes"
                print "reverse %d %d" % (lIdx + 1, rIdx + 1)
            else:
                print "no"

if __name__ == "__main__":
    n = raw_input()
    nums = map(int, raw_input().split(" "))
    checkAlmostSotrted(nums)

