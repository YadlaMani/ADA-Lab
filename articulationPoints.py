from collections import defaultdict

def build_graph():
    graph = defaultdict(list)
    n = int(input("Enter the number of nodes: "))
    e = int(input("Enter the number of edges: "))
    
    for _ in range(e):
        print("Enter edges in the format: start end")
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)
    
    return graph
def dfs(node,parent,time,tin,low,visited,mark,graph):
    visited[node]=True
    tin[node]=low[node]=time[0]
    time[0]+=1
    child_count=0
    for neighbor in graph[node]:
        if neighbor == parent:
            continue
        if not visited[neighbor]:
            dfs(neighbor,node,time,tin,low,visited,mark,graph)
            low[node]=min(low[node],low[neighbor])
            if low[neighbor] >= tin[node] and parent is not None:
                mark[node] = 1
            child_count += 1
        else:
              low[node] = min(low[node], tin[neighbor])
    if parent is None and child_count > 1:
        mark[node] = 1
        

def find(graph):
    visited = {node: False for node in graph}
    tin = {node: -1 for node in graph}
    low = {node: -1 for node in graph}
    mark = {node: 0 for node in graph}
    timer = [1] 
    for node in graph:
        if not visited[node]:
            dfs(node, None, timer, tin, low, visited, mark, graph)
    articulation_points = [node for node in graph if mark[node] == 1]
    return articulation_points if articulation_points else [-1]
graph=build_graph()
articulationPoints=find(graph)
print("Articulation Points:")
if(articulationPoints==[-1]):
    print("No articulation Points")
else:
    for point in articulationPoints:
        print(point,end=" ")