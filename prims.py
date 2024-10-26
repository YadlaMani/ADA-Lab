import heapq
def build_graph():
    graph={}
    n=int(input("Enter the number of nodes:"))
    for i in range(n):
        node=input("Enter node name:")
        graph[node]={}
    e=int(input("Enter no.of edges:"))
    for i in range(e):
        print("Enter edges in the format: start end weight")
        u,v,wt=input().split()
        wt=int(wt)
        graph[u][v]=wt
        graph[v][u]=wt
    return graph

def prims(graph,start):
    visited=set()
    mst=[]
    total_wei=0
    priority_queue=[(0,start,None)]  #weight,node,parent
    while priority_queue and len(visited) < len(graph):
        wei,cur,parent=heapq.heappop(priority_queue)
        if cur in visited:
            continue
        visited.add(cur)
        if(wei):
            mst.append((parent,cur,wei))
            total_wei+=wei
        for neighbor,wt in graph[cur].items():
            if neighbor not in visited:
                heapq.heappush(priority_queue,{wt,neighbor,cur})
    return mst,total_wei

graph=build_graph()
start = input("Enter the start node: ")
mst,wei=prims(graph,start)
print(f"Minimum Spanning Tree (MST) starting from {start}:")
for u,v,wt in mst:
    print(f"{u}-{v}:{wt}")
print(f"Total weight of the mst:{wei}")