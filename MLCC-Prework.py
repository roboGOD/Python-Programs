###################################
###								###
### Ishwer Kumar				###
### Roll No. : 11501048			###
### Punjabi University, Patiala ###
###								###
###################################


####################################################
### 1. Defining and calling functions, using positional and keyword parameters

print "\n1. Defining and calling functions, using positional and keyword parameters"

def foo(a, mul=1, add=0):	# Declaration of arguments
	return a*mul+add

print foo(10)				# Positional Argument -> a=10 
print foo(10, 2)			# Positional Argument -> a=10, mul=2
print foo(10, add=5)		# Positional -> a=10 and Keyword Argument -> add=5
print foo(10, add=3, mul=2)	# Here Position Doesn't matter


#####################################################
### 2. Dictionaries, lists, sets (creating, accessing, and iterating)

print "\n2. Dictionaries, lists, sets (creating, accessing, and iterating)"

### Lists
print "\nList:"
ls = [2, 3, 4]
print ls[2]
for i in ls:
	print i

### Dictionaries
print "\nDictionary:"
d = {"roboGOD": 11501048, "Kira": 11501037, "Amway": 11501039, "vRock": 11501068}
print d["roboGOD"]
for i in d:
	print i, d[i] # Prints all the keys and corresponding values

### Sets
print "\nSets:"
s = set([10,20,30])
if 10 in s:
	print "10 is in the set."
if 90 not in s:
	print "90 is not in the set."
for i in s:
	print i
s.add(10)	# length of set won't increase since 10 is already in the set
s.add(40)	# length of set will increase as 40 will be added to the set

#####################################################
### 3. for loops, for loops with multiple iterator variables (e.g., for a, b in [(1,2), (3,4)])

print "\n3. for loops, for loops with multiple iterator variables (e.g., for a, b in [(1,2), (3,4)])"

a = [10, 20, 30]
b = [1, 2, 3]
for i, j in zip(b,a):	# Iterates through both the arrays at the same time
	print i, j


#####################################################
### 4. if/else conditional blocks and conditional expressions

print "\n4. if/else conditional blocks and conditional expressions"

a = 10
b = 20
c = 20
### If-Else logic to find the greatest of three
if a < b:
	if a < c:
		print a, "is the smallest."
	elif a > c:
		print c, "is the smallest."
	else:
		print a, "is equals to", c, "and both are smallest."
else:
	if b < c:
		print b, "is the smallest."
	elif b > c:
		print c, "is the smallest."
	else:
		print b, "is equal to", c, "and both are smallest."

#####################################################
### 5. String formatting (e.g., '%.2f' % 3.14)

print "\n5. String formatting (e.g., '%.2f' % 3.14)"

name = "roboGOD"
print "I am %s" % name

c = 3.234532672
print c, "becomes %.2f" % c
b = 4.9987434
print b, "becomes %.2f" % b

a = 9
print "Binary of %d is %s" % (a, format(a, 'b'))


#####################################################
### 6. Variables, assignment, basic data types (int, float, bool, str)

print "\n6. Variables, assignment, basic data types (int, float, bool, str)"

print  "All of these are demonstrated above."



#####################################################
### 7. The pass statement

print "\n3. The pass statement"
### Printing only odd numbers
for i in range(20):
	if i%2==0:
		pass		# If i is even do nothing, "pass"
	else:
		print i,
print ""


#####################################################
### 8. List comprehensions
print "\n8. List Comprehensions"
'''
List comprehensions provide a concise way to create lists. Common applications are to make new 
lists where each element is the result of some operations applied to each member of another 
sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.
'''
### For example, to create a list of squares
sq = [x**2 for x in range(1,11)]
print sq

### Also we can use two for loops
print [(x,y) for x in [10,20,30] for y in [20,30,40] if x != y]

### Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

print [[row[i] for row in matrix] for i in range(4)]

#####################################################
### 9. Lambda functions
'''
Small anonymous functions can be created with the lambda keyword. 
This function returns the sum of its two arguments: lambda a, b: a+b 
Lambda functions can be used wherever function objects are required. 
They are syntactically restricted to a single expression. Semantically, 
they are just syntactic sugar for a normal function definition. Like nested 
function definitions, lambda functions can reference variables from the containing scope.
'''

### Lambda expression to create incrementor
inc = lambda x: x+2		# Takes an input x as argument and returns incremented value by 2
print inc(1)
print inc(2)
print inc (10)

### Sort using different keys
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1]) 	# Here, key becomes a function which takes a pair as input and returns the 2nd element.
print pairs
