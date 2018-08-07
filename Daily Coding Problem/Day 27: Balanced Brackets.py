'''
	This problem was asked by Facebook.
	
	Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
	For example, given the string "([])[]({})", you should return true.
	Given the string "([)]" or "((()", you should return false.

'''

def findMatch(c):
	if c == ')':
		return '('
	elif c == '}':
		return '{'
	elif c == ']':
		return '['
	else:
		return 'Z'

def isOpenBracket(i):
	if i == '(' or i == '{' or i == '[':
		return True
	return False


def balancedBrackets(b):

	stack = [None]
	for i in b:
		if isOpenBracket(i):
			stack.append(i)
		else:
			last = stack.pop(len(stack)-1)
			
			if last == None:
				return False
			elif findMatch(i) == last:
				continue
			else:
				return False

	last = stack.pop(len(stack)-1)

	if last == None:
		return True 

	return False



if __name__ == '__main__':

	print (balancedBrackets(raw_input()))
