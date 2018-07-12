

def numberOfWays(N,s):
	global d
	if N == 0:
		### We have found one(1) way to reach the top
		return 1
	### If we have already found it.
	if N in d:
		return d[N]
	result = 0
	for i in s:
		if N-i > 0:
			### Add number of ways found recursively
			result += numberOfWays(N-i,s)
	d[N] = result
	return result

### Here's a faster and non recursive solution

def numsOfWays(N,s):
	if N == 0:
		return 1
	nums = [0]*(N+1)
	nums[0] = 1
	for i in range(1,N+1):
		total = 0
		for j in s:
			if i-j >= 0:
				total += nums[i-j]
		nums[i] = total
	return nums[N]

if __name__ == '__main__':
	N = None
	s = []
	global d 
	d = {}
	while True:
		try:
			temp = raw_input("Enter N or 0 to Stop: ")
			if temp == "":
				print "Alright, Exiting..."
				break
			N = int(temp)
			if N <= 0:
				print "Alright, Exiting..."
				break
			s = map(int, raw_input("Enter Set: ").split())
		except Exception:
			continue
		nOW = numsOfWays(N,s)
		print "Number of Ways:", nOW
		print ""