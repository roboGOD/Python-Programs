'''
	This problem was asked by Twitter.

	Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, 
	return all strings in the set that have s as a prefix.

	For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

	Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

'''


def prefixQueries(s, queries):
	n = len(s)
	result = []
	for i in queries:
		temp = i[:n]
		if temp == s:
			result.append(i)
	return result

if __name__ == '__main__':
	s = raw_input("Enter s: ")
	n = int(raw_input("Enter n: "))
	arr = []
	print "Enter", n, "queries:"
	for _ in range(n):
		arr.append(raw_input())
	print "\nList of strings:"
	result = prefixQueries(s, arr)
	for _ in result:
		print _
