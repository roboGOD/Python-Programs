def isPrime(n):
	if n==2 or n==3:
		return True
    if n < 2 or n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

if isPrime(int(raw_input())):
    print "YES!"
else:
    print "NO!"