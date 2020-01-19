
def computeWithBreadthFirstSearch(Graph,index):
    setUV = [-1] * len(Graph)
    setUV[index] = 1
    queue = []
    queue.append(index)
    while queue:
        U = queue.pop()
        if Graph[U][U] == 1:
            return False
        for V in range(len(Graph)):
            if Graph[U][V] == 1 and setUV[V] == -1:
                setUV[V] = 1 - setUV[U]
                queue.append(V)
            elif Graph[U][V] == 1 and setUV[V] == setUV[U]:
                return False
    return True
def isBipartite(Graph):
    print()
    for i in range(len(Graph)):
        print(Graph[i])
    print()
    isBipartiteOrNot = computeWithBreadthFirstSearch(Graph,0)
    if isBipartiteOrNot:
        print("Yes")
    else:
        print("No")

Graph=[[0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0]]

isBipartite(Graph)

Graph2=[[0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]]

isBipartite(Graph2)


Graph3=[[0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0]]

isBipartite(Graph3)