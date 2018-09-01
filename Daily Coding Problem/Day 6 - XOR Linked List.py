'''
	This problem was asked by Google.

	An XOR linked list is a more memory efficient doubly linked list. 
	Instead of each node holding next and prev fields, it holds a field named both, 
	which is an XOR of the next node and the previous node. Implement an XOR linked 
	list; it has an add(element) which adds the element to the end, and a get(index) 
	which returns the node at index.
	
	If using a language that has no pointers (such as Python), you can assume you have 
	access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

'''

class Node:
	counter = 0
	id_to_node = {}
	node_to_id = {}
	
	def __init__(self, val, npx=None):
		self.info = val
		self.npx = npx
		Node.counter += 1
		self.id = Node.counter
		Node.id_to_node[self.id] = self
		Node.node_to_id[self] = self.id

def ref(obj):
	return Node.node_to_id[obj]

def deref(num):
	return Node.id_to_node[num]


class XORList:
	def __init__(self):
		self.Head = None

	def add(self, val):
		if self.Head == None:
			self.Head = Node(val)
		else:
			prev = None
			cur = self.Head
			nxt = None
			while cur.npx != (prev):
				if prev == None:
					nxt = deref(cur.npx)
				else:
					nxt = deref(prev ^ cur.npx)
				prev = ref(cur)
				cur = nxt
			if prev == None:
				cur.npx = ref(Node(val, ref(cur)))
			else:
				cur.npx = prev ^ ref(Node(val, ref(cur)))

	def getNode(self, ind):
		if self.Head == None:
			return None
		else:
			count = 0
			if ind == count:
				return self.Head
			prev = None
			cur = self.Head
			nxt = None
			while cur.npx != prev:
				if prev == None:
					nxt = deref(cur.npx)
				else:
					nxt = deref(prev ^ cur.npx)
				prev = ref(cur)
				cur = nxt
				count += 1 
				if count == ind:
					return cur
			return None

	def display(self):
		if self.Head == None:
			print "No elements."
		else:
			prev = None
			cur = self.Head
			nxt = None
			print "Elements:",
			while cur.npx != prev:
				print cur.info,
				if prev == None:
					nxt = deref(cur.npx)
				else:
					nxt = deref(prev ^ cur.npx)
				prev = ref(cur)
				cur = nxt
			print cur.info

X = XORList()
arr = map(int, raw_input("Enter Elements: ").split())
for i in arr:
	X.add(i)

while True:
	a = int(raw_input("\n1. Print\n2. Add\n3. Get\n4. Exit.\nSelect: "))
	if a == 1:
		print ""
		X.display()
	elif a == 2:
		X.add(int(raw_input("Enter Element: ")))
	elif a == 3:
		s = X.getNode(int(raw_input("Enter Index: ")))
		print ""
		if s == None:
			print "Index out of range."
		else:
			print "Element is", s.info
	elif a == 4:
		print "Exiting..."
		break
	else:
		print ""
		print "Invalid Option."



