'''
You are given a square grid with some cells open (.) and some blocked (X). 
Your playing piece can move ALONG ANY ROW OR COLUMN until it reaches the edge of the grid or a blocked cell. 
Given a grid, a start and an end position, determine the number of minimum moves it will take to get to the end position.

Note: If moving in same direction the whole thing must be counted as 1. This is called a Superman Move.
'''


"YES!!"

class Graph:
    def __init__(self):
        self.graph = {}
        self.tupleList = {}
        self.counter = 0
    
    def addEdge(self, u, v):
        if u not in self.tupleList:
            self.tupleList[u] = self.counter
            self.counter += 1
        if v not in self.tupleList:
            self.tupleList[v] = self.counter
            self.counter += 1
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        
    
    def displayGraph(self):
        for i in sorted(self.graph.keys()):
            print i, "::", self.graph[i]
    

    ### This was my way
    '''
    def performBFS(self, Head, Target):
        visited = [False] * len(self.graph)
        print "Head:", Head, "& Target:", Target
        queue = []
        levels = [] #In Case Counting Each Individual Step and not the Superman Moves
        #steps = 0

        ### Creating Path
        tempPath = []
        
        queue.append(Head)
        visited[self.tupleList[Head]] = True
        while queue:
            s = queue.pop(0)
            tempPath.append(s)
            #if len(levels) != 0:
            #    print s, "::", levels[len(levels)-1]
            """
            levels[0] -= 1
            if levels[0] == 0:
                ### In Case Counting Each Individual Step and not the Superman Moves, Uncomment following; and comment others
                steps += 1
                levels.pop(0)
            """

            if s == Target:
                path = []
                parent = None
                child = None
                for i in range(len(tempPath)-1,-1,-1):
                    j = tempPath[i]
                    if i == len(tempPath)-1:
                        child = j
                        path.append([j])
                        #levels.pop()
                    else:
                        try:
                            temp = levels.pop()
                        except Exception:
                            continue
                        tempList = []
                        for k in range(temp):
                            parent = tempPath[i-k]
                            if child in self.graph[parent]:
                                tempList.append(parent)

                        if tempList != []:
                            path.append(tempList)
                            child = tempList[0]        
                            i = i - temp + 1
                path = path[::-1]
                return path

            tempCount = 0
            for i in self.graph[s]:
                if visited[self.tupleList[i]] != True:
                    queue.append(i)
                    visited[self.tupleList[i]] = True
                    tempCount += 1
            levels.append(tempCount)
        return -1
    '''

    ### This is High Way
    def performBFS(self, Head, Target):
        visited = [False] * len(self.graph)
        queue = []
        dis = {}

        queue.append(Head)
        visited[self.tupleList[Head]] = True
        dis[Head] = 0    # Distance of every node from Head
        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                if visited[self.tupleList[i]] != True:
                    queue.append(i)
                    visited[self.tupleList[i]] = True
                    ### Obviously Distance(Moves) will increment if we move from one node to another
                    ### Note:: We are keeping a record of every possible move of castle(Hathi) in a chess board
                    ### So all the nodes will have multiple edges denoting the moves
                    dis[i] = dis[s] + 1
        return dis


# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    Head = (startX, startY)
    Target = (goalX, goalY)
    
    G = Graph()
    
    ### This was My way
    '''
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 'X':
                if j+1 < n:
                    if grid[i][j+1] != 'X':
                        G.addEdge((i,j), (i,j+1))
                        G.addEdge((i,j+1), (i,j))
                if i+1 < n:
                    if grid[i+1][j] != 'X':
                        G.addEdge((i,j), (i+1,j))
                        G.addEdge((i+1,j), (i,j))
    '''

    ### This is High Way
    ### So, In Short... Instead of Adding just the adjacent cells as Edges, add all the possible
    ### moves of castle(Hathi) in chess board. So we will give it a lot of flexibility of movement
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 'X':
                for k in range(i-1,-1,-1):
                    if grid[k][j] == '.':
                        G.addEdge((i,j), (k,j))
                        #G.addEdge((k,j), (i,j))
                    else:
                        break
                for k in range(i+1,n):
                    if grid[k][j] == '.':
                        G.addEdge((i,j), (k,j))
                        #G.addEdge((k,j), (i,j))
                    else:
                        break
                for k in range(j-1,-1,-1):
                    if grid[i][k] == '.':
                        G.addEdge((i,j), (i,k))
                        #G.addEdge((i,k), (i,j))
                    else:
                        break
                for k in range(j+1,n):
                    if grid[i][k] == '.':
                        G.addEdge((i,j), (i,k))
                        #G.addEdge((i,k), (i,j))
                    else:
                        break


    dis = G.performBFS(Head, Target)

    if Target in dis:
        return dis[Target]
    else:
        return -1
    #G.displayGraph()
    #path =  G.performBFS(Head,Target)
    #print path

    ### This was obviously my way
    '''
    isImove = None
    prev = None
    mini = 0
    for i in path:
        if prev == None:
            pass
        elif isImove == None:
            if i[0] != prev[0]:
                isImove = True
            elif i[1] != prev[1]:
                isImove = False
        elif isImove:
            if i[1] != prev[1]:
                isImove = False
                mini += 1
        elif not isImove:
            if i[0] != prev[0]:
                isImove = True
                mini += 1
        prev = i

    mini += 1

    return mini
    '''

                
            

if __name__ == '__main__':

    n = int(raw_input())

    grid = []

    for _ in xrange(n):
        grid_item = raw_input()
        grid.append(grid_item)

    startXStartY = raw_input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    print "Minimum Moves:", result
