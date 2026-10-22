def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
graph = {i: [] for i in range(n)}
print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) 
start = int(input("Enter starting vertex: "))
visited = set()
print("DFS Traversal:", end=" ")
dfs(graph, start, visited)
