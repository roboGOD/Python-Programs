


def countLoops(nodes, edges, matrix):
	global count
	graph = {}
	for i in range(nodes):
		graph[i+1] = []
	for i in matrix:
		u, v, e = i
		graph[u].append((v,e))

	visEdge = set()
	visNode = set()
	count = 0

	def DFS(node):
		global count
		for i in graph[node]:
			if i[0] not in visNode:
				visEdge.add(i[1])
				visNode.add(i[0])
				DFS(i[0])
			elif i[1] in visEdge:
				pass
			else:
				visEdge.add(i[1])
				count += 1

	visNode.add(1)
	DFS(1)

	return count


if __name__ == '__main__':
	n = int(raw_input())
	e = int(raw_input())
	mat = []
	for _ in range(e):
		mat.append(map(int, raw_input().split()))

	print countLoops(n, e, mat)





