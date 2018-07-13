'''
	Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
	For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
	Bonus: Can you do this in one pass?

'''

def sumIsK(ls, k):
	d = {}
	for i in ls:
		if i in d:
			return True
		d[k-i] = 1
	return False

if __name__ == '__main__':
	n,k = map(int, raw_input().split())
	ls = map(int, raw_input().split())
	if sumIsK(ls, k):
		print "Yes!"
	else:
		print "Nope."
