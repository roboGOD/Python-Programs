'''

	This problem was asked by Google.
	A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
	Given the root to a binary tree, count the number of unival subtrees.
	For example, the following tree has 5 unival subtrees:

   		0
  	   / \
 	  1   0
    	 / \
   		1   0
  	   / \
	  1   1

'''

class Node:
	def __init__(self, val, left=None, right=None):
		self.data = val
		self.left = left
		self.right = right


class Tree:
	def __init__(self):
		self.root = None

	def createTree(self, temp=None):
		if temp == None:
			self.root = Node(int(raw_input("Enter value of root: ")))
			temp = self.root
		print "left  child of", temp.data, "\t:",
		val = int(raw_input())
		if val == 42:
			return
		if val != -1:
			temp.left = Node(val)
		print "right child of", temp.data, ":",
		val = int(raw_input())
		if val == 42:
			return
		if val != -1:
			temp.right = Node(val)
		if temp.left != None:
			self.createTree(temp.left)
		if temp.right != None:
			self.createTree(temp.right)

	def displayValues(self, temp=42):
		if temp == 42:
			temp = self.root
		if temp == None:
			print "No values in tree."
		queue = []
		queue.append(self.root)
		print "Tree:",
		while queue:
			temp = queue.pop(0)
			if temp == None:
				print "null",
			else:
				print temp.data,
				queue.append(temp.left)
				queue.append(temp.right)
		print ""


def countUniValSubtrees(tree):
	pass


t = Tree()
t.createTree()
#t.displayValues()








		