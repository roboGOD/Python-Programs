'''
	This problem was asked by Facebook.

	Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
	For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
	You can assume that the messages are decodable. For example, '001' is not allowed.

'''


def decodingWays(s):
	count = 1
	countDict = {}
	for i in range(len(s)-1):
		if int(s[i]+s[i+1]) <= 26:
			if i <= 1:
				count += 1
			elif i > 1:
				count += countDict[s[:i]]
		countDict[s[:i+2]] = count
	return count



s = raw_input("Enter Encoded Message: ")
c = decodingWays(s)
print "Number of Ways:", c

