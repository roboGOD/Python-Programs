from time import time

def nthPrime(n):
	primes = []  # List of All Prime Numbers
	i = 3        # We know 2 is prime.. so we start from three and ignore all even numbers except 2
	primes.append(2) # 2 is prime
	k = 1        # Keeps the count of prime numbers found
	while k<n:   # Loop over k not i
		isPrime = True     # i refers to the integers which we need to check for prime or not
		for z in primes:   # for every prime that we have fount,	
			if i%z == 0:   # if i is divisible any of them, then i is not prime
				isPrime = False
				break
			if 2*z > i:    # break out of the loop if the prime number is greater than half of i
				break
		if isPrime:        # if it's prime, append it to list of primes
			primes.append(i)
			k+=1			
		i+=2				# Ignore even numbers, so increment by 2
	return primes[-1] # Return the nth prime number, Indexing is cool in Python 


def nthFib(n):
	a = 0
	b = 1
	i = 1
	while i < n:
		a, b = b, (a+b)
		i += 1
	return b

def findNth(n):
	if n%2 == 0:
		return nthPrime(int(n/2))
	else:
		return nthFib(int(n/2)+1)

if __name__=='__main__':

	### Test Code
	'''
	for i in range(1,30):
		print findNth(i)
	'''

	n = int(raw_input())
	t1 = time()
	print findNth(n)
	print str((time()-t1)) + "s"







