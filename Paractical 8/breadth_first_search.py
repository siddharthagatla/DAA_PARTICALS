
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
graph = {i: [] for i in range(n)}
print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  
start = int(input("Enter starting vertex: "))
bfs(graph, start)
