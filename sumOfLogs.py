import math


a = int(raw_input())

summ = 0
for i in range(1,a+1):
	summ += math.log(i, a)

print summ

