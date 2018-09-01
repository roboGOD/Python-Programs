'''
	Given the root to a binary tree, implement serialize(root), 
	which serializes the tree into a string, and deserialize(s), 
	which deserializes the string back into the tree.

	For example, given the following Node class

		class Node:
    		def __init__(self, val, left=None, right=None):
        		self.val = val
        		self.left = left
        		self.right = right

	The following test should pass:

		node = Node('root', Node('left', Node('left.left')), Node('right'))
		assert deserialize(serialize(node)).left.left.val == 'left.left'

'''
from __future__ import print_function

count = 0
node_count = None

class Node:
	def __init__(self, val=None, left=None, right=None):
		global count
		self.val = val
		self.left = left
		self.right = right
		count += 1

	def displayTree(self):
		global node_count
		node_count += 1
		if node_count == 1:
			print(self.val)
		else:
			print("_:",self.val)
		#print "|"
		if self.left != None:
			print("|",end="")
			s = '__'*(node_count-1)
			if node_count-1 != 0:
				print(s,end="")
			self.left.displayTree()
			node_count -= 1
		
		elif self.left == None:
			s = '__'*(node_count-1)
			print("|",end="")
			print(s,end="")
			print("_: Null")
		

		if self.right != None:
			print("|",end="")
			s = '__'*(node_count-1)
			if node_count-1 != 0:
				print(s,end="")
			self.right.displayTree()
			node_count -= 1
		
		elif self.right == None:
			s = '__'*(node_count-1)
			print("|",end="")
			print(s,end="")
			print("_: Null")

	def display(self):
		global node_count 
		node_count = 0
		self.displayTree()

def serializer(node, ls):
		
	ls.append(node.val)
	if node.left == None:
		ls.append("Null")
	else:
		ls = serializer(node.left, ls)
	if node.right == None:
		ls.append("Null")
	else:
		ls = serializer(node.right, ls)
	return ls


def serialize(node):
	ls = []
	ls = serializer(node, ls)
	s = " ".join(ls)
	return s

def deserializer(ls, n1):
	if len(ls) <= 0:
		return n1
	
	if ls[0] == "Null":
		n1 = None
		ls.pop(0)
		return n1
		
	n1.val = ls[0]
	ls.pop(0)
		
	n1.left = deserializer(ls, Node())
	n1.right = deserializer(ls, Node())

	return n1

def deserialize(s):
	ls = s.split()
	n1 = deserializer(ls, Node())
	return n1



n1 = Node('root',Node('left', Node('left.left'), Node('left.right')), Node('right', None, Node('right.right')))
print("##########################################################")
print("Before Serialization:: ")
n1.display()
print("\n##########################################################")
print("After Serialization and Deserialization:: ")
deserialize(serialize(n1)).display()

#node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left', "Oh, Fuck It!!!"
