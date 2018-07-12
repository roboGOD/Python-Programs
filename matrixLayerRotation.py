#!/bin/python

##########################################################################################################3
'''
    You are given a 2D matrix, a, of dimension MxN and a positive integer R. 
    You have to rotate the matrix R times and print the resultant matrix. 
    Rotation should be in anti-clockwise direction. 
    It is guaranteed that the minimum of M and N will be even. 
'''

class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        '''
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        '''
        self.graph[u] = v

    def displayGraph(self):
        print "Edges Are:"
        for i in sorted(self.graph.keys()):
            print i, ":", self.graph[i]
        print ""

    def createRing(self, matrix, level):
        m = len(matrix)
        n = len(matrix[0])
        i = level
        for j in range(level,n-level):
            if j+1 < n-level:
                #n1 = i*n + j
                #n2 = i*n + j-1
                n1 = (i,j)
                n2 = (i,j+1)
                self.addEdge(n1,n2)
                #self.addEdge(n2,n1)
        i = m-level-1
        for j in range(level,n-level):
            if j-1 >= level:
                #n1 = i*n + j
                #n2 = i*n + j+1
                n1 = (i,j)
                n2 = (i,j-1)
                self.addEdge(n1,n2)
                #self.addEdge(n2,n1)
        j = level
        for i in range(level,m-level):
            if i-1 >= level:
                #n1 = i*n + j
                #n2 = (i+1)*n + j
                n1 = (i,j)
                n2 = (i-1,j)
                self.addEdge(n1,n2)
                #self.addEdge(n2,n1)
        j = n-level-1
        for i in range(level,m-level):
            if i+1 < m-level:
                #n1 = i*n + j
                #n2 = (i-1)*n + j
                n1 = (i,j)
                n2 = (i+1,j)
                self.addEdge(n1,n2)
                #self.addEdge(n2,n1)

    
    def rotateRing(self, r, levels):
        Heads = {}
        for i in levels:
            #Head = i*n+i
            maxRot = m-2*i-1 + n-2*i-1 + m-2*i-1 + n-2*i-2 + 1
            actualRot = r%maxRot
            Head = (i,i)
            for _ in range(actualRot):
                Head = self.graph[Head]
            Heads[i] = Head

        return Heads

    def rotatedMatrix(self, matrix, Heads):
        m = len(matrix)
        n = len(matrix[0])
        rotated = [ [0]*n for _ in xrange(m) ]

        for level, Head in Heads.items():
            temp = Head

            i = level
            for j in range(level,n-level):
                #print temp
                rotated[i][j] = matrix[temp[0]][temp[1]]
                #print "(",i,",",j,")",
                temp = self.graph[temp]
            #print ""

            j = n-level-1
            for i in range(level+1,m-level):
                #print temp
                rotated[i][j] = matrix[temp[0]][temp[1]]
                #print "(",i,",",j,")",
                temp = self.graph[temp]
            #print ""

            i = m-level-1
            for j in range(n-level-2,level-1,-1):
                #print temp
                rotated[i][j] = matrix[temp[0]][temp[1]]
                #print "(",i,",",j,")",
                temp = self.graph[temp]
            #print ""

            j = level
            for i in range(m-level-2,level,-1):
                #print temp
                rotated[i][j] = matrix[temp[0]][temp[1]]
                #print "(",i,",",j,")",
                temp = self.graph[temp]
            #print ""

        return rotated



# Complete the matrixRotation function below.
def matrixRotation(matrix, m, n, r):
    level = min(m,n)/2
    levels = []
    G = Graph()
    
    for i in range(level):
        levels.append(i)
        G.createRing(matrix, i)

    #G.displayGraph()
    Heads = G.rotateRing(r, levels)

    ### Constructing the rotated matrix
    rotated = G.rotatedMatrix(matrix, Heads)
    print "\nRotated Matrix:"
    for i in range(m):
        for j in range(n):
            print rotated[i][j],
        print ""




if __name__ == '__main__':
    mnr = raw_input().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in xrange(m):
        matrix.append(map(int, raw_input().rstrip().split()))

    matrixRotation(matrix, m, n, r)