'''
	This problem was asked by Stripe.

	Given an array of integers, find the first missing positive integer in linear time and 
	constant space. In other words, find the lowest positive integer that does not exist in 
	the array. The array can contain duplicates and negative numbers as well.
	For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
	You can modify the input array in-place.
'''

def findMissingInteger(arr):
	k = None
	i = 0
	while i < len(arr):
		if arr[i] <= 0:
			del arr[i]
			continue
		i += 1

	for i in range(len(arr)):
		if abs(arr[i]) <= len(arr):
			arr[abs(arr[i])-1] *= (-1)

	missingInt = None
	for i in range(len(arr)):
		if arr[i] > 0:
			missingInt = i+1
			break

	if missingInt == None:
		missingInt = len(arr)+1

	return missingInt


	

	### Here's my not-so-good implementation which has a lot of bugs.
	'''
	lower = 1
	missingInt = 1
	upper = None
	greaterUpper = None
	for i in arr:
		if i <= 0:
			continue
		elif i == missingInt:
			lower += 1
			missingInt = lower
			if upper == None:
				continue
			elif lower == upper-1:
				lower = upper
				upper = greaterUpper
				if upper != None:
					if upper-lower == 1:
						lower = upper
						upper = None
				greaterUpper = None
		elif i == lower+1:
			if upper == None:
				lower += 1
			elif i != upper-1:
				lower += 1
			elif i == upper-1:
				lower = upper
				upper = greaterUpper
				if upper != None:
					if upper-lower == 1:
						lower = upper
						upper = None
				greaterUpper = None
		elif i < lower+1:
			continue
		elif i > lower+1:
			if upper == None:
				upper = i
			elif i == upper:
				continue
			elif i == upper-1:
				if greaterUpper == None:
					greaterUpper = upper
					upper = i
				else:
					upper = i
			elif i == upper+1:
				if greaterUpper == None:
					greaterUpper = i
				else:
					continue
			elif i > upper:
				continue
			elif i < upper:
				greaterUpper = None
				upper = i

	return missingInt
	'''


missingInt = findMissingInteger(map(int, raw_input("Enter array: ").split()))
print "Missing Integer:", missingInt
