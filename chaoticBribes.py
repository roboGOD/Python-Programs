#!/bin/python

'''
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride!
There are a number of people queued up, and each person wears a sticker indicating their 
initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to n at the back.
Any person in the queue can bribe the person directly in front of them to swap positions. 
If two people swap positions, they still wear the same sticker denoting their original 
places in line. One person can bribe at most two others.

For example, if n=8 and 5 bribes 4, the queue will look like this: 1,2,3,5,4,6,7,8.
Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place 
to get the queue into its current state!

'''
# Complete the minimumBribes function below.
def recursiveBribe(i,q):
    inc = 0
    j = q[i]
    diff = j-i-1
    if diff > 2:
        return -1, q
    elif diff > 0:
        if q[i] > q[i+1]:
            inc += 1
            q[i] = q[i+1]
            q[i+1] = j
        else:
            tInc, q = recursiveBribe(i+1,q)
            if tInc == -1:
                return -1,q
            inc += tInc
        if diff == 2:
            if q[i+1] > q[i+2]:
                inc += 1
                temp = q[i+1]
                q[i+1] = q[i+2]
                q[i+2] = temp
            else:
                tInc, q = recursiveBribe(i+2,q)
                if tInc == -1:
                    return -1,q
                inc += tInc
    elif diff == 0:
        pass
    return inc,q
            
        

def minimumBribes(q):
    minB = 0
    i = 0
    while i < len(q):
        j = q[i]
        diff = j-i-1
        if diff > 2:
            print "Too chaotic"
            break
        elif diff == 0:
            pass
        else:
            inc,q = recursiveBribe(i,q)
            if inc == -1:
                print "Too chaotic"
                break
            minB += inc
            i -= 1
        i += 1
    if i == len(q):
        print minB
if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
