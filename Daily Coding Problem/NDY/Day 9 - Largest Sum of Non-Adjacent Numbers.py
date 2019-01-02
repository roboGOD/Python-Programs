'''
	This problem was asked by Airbnb.

	Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
	For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
	
	Follow-up: Can you do this in O(N) time and constant space?

'''

def largestSum(a):
	lSum = 0
	i = 0
	while i < len(a)-1:
		if a[i] <= 0:
			i += 1
			continue
		elif a[i] > a[i+1]:
			lSum += a[i]
			i += 2
			continue
		elif a[i] < a[i+1]:
			if i+2 == len(a):
				lSum += a[i+1]
				#print "Yoohoo"
				break
			elif a[i+1] < a[i+2]:
				lSum += a[i]
				i += 2
				continue
			elif a[i+1] > a[i+2]:
				lSum += a[i+1]
				i += 3
				continue
			elif a[i+1] == a[i+2]:
				i += 1
				continue
		elif a[i] == a[i+1]:
			if i+2 == len(a):
				lSum += a[i]
				i += 2
				break
			elif i+2 == len(a)-1:
				lSum += a[i]
				i += 2
				break
			else:
				lSum += a[i]
				i += 2
				continue
	if i == len(a)-1:
		if a[i]>0:
			lSum += a[i]
	return lSum


if __name__ == '__main__':
	arr = map(int, raw_input().split())
	print largestSum(arr)
