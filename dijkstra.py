import heapq
def buildGraph():
    graph={}
    nV=int(input("Enter number of nodes:"))
    for i in range(nV):
        node=input("Enter node name:")
        graph[node]={}
    nE=int(input("Enter no.of edges"))
    print("Enter edges in the format: start end weight")
    for i in range(nE):
        u,v,wt=input().split()
        wt=int(wt)
        graph[u][v]=wt
        graph[v][u]=wt
    return graph

def dijkstra(graph,start):
    distances = {node: float('inf') for node in graph}
    distances[start]=0
    priority_queue = [(0, start)]
    while priority_queue:
        currDis,currNode=heapq.heappop(priority_queue)
        if currDis>distances[currNode]:
            continue
        for neigh,wei in graph[currNode].items():
            distance=currDis+wei
            if distance < distances[neigh]:
                distances[neigh]=distance
                heapq.heappush(priority_queue, (distance, neigh))
    return distances


graph=buildGraph()
start=input("Enter the start node:")
shortestPaths=dijkstra(graph,start)
print(f"Shortest paths from {start}: {shortestPaths}")