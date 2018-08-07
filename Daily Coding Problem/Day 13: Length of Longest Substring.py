'''
	This problem was asked by Amazon.

	Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
	For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

'''

def lengthOfSubstring(s, k):
	n = len(s)
	if k >= n:
		return n

	maxLen = k
	window = k+1
	while window <= n:
		continue_flag = False
		
		for i in range(0, n-window+1):
			found_flag = False
			countChar = 0
			seen = {}
			
			for j in range(i, i+window):
				found_flag = True
				if s[j] in seen:
					pass
				else:
					countChar += 1
					seen[s[j]] = 1
				if countChar > k:
					found_flag = False
					break

			del seen
			if found_flag:
				maxLen = window
				continue_flag = True
				break

		if not continue_flag:
			break
		window += 1

	return maxLen


if __name__ == '__main__':

	s = raw_input()
	k = int(raw_input())
	print lengthOfSubstring(s, k)




