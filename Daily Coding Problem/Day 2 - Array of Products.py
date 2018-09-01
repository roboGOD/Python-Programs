'''
	Given an array of integers, return a new array such that each element at index i of the 
	new array is the product of all the numbers in the original array except the one at i.
	For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
	If our input was [3, 2, 1], the expected output would be [2, 3, 6].
	
	Follow-up: what if you can't use division?
'''

''' Solution:
	Doing it without division was tricky.
	I had to create two different arrays n1 and n2 in the first loop where n1 contains successive multiplications
	of elements of given array from 0 to n-1 and n2 contains successive multiplications of elements of given array
	from n-1 to 0. There's an extra '1' in the begining of both array which is meant to ignore the elements on the
	edge. Like First and Last element of array.

	So, overall complexity is O(2n). Not Bad Huh.
'''

def arrayOfProducts(array):
	n1 = [1]
	n2 = [1]
	n = len(array)
	for i in range(n):
		n1.append(n1[i]*array[i])
		n2.append(n2[i]*array[n-1-i])

	new_array = [0]*n
	for i in range(n):
		#print n1[i], "*", n2[len(n2)-2-i]
		new_array[i] = n1[i]*n2[len(n2)-2-i]

	return new_array


print arrayOfProducts(map(int, raw_input().split()))