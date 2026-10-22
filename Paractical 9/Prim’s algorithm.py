
# Prim's Algorithm using user input

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = []

print("Enter edges as: source destination weight")

for i in range(e):
    u, v, w = map(int, input().split())
    graph.append((u, v, w))

visited = [False] * n
visited[0] = True

mst = []
total_cost = 0

while len(mst) < n - 1:
    min_weight = float('inf')
    selected_edge = None

    for u, v, w in graph:
        if visited[u] and not visited[v]:
            if w < min_weight:
                min_weight = w
                selected_edge = (u, v, w)

        elif visited[v] and not visited[u]:
            if w < min_weight:
                min_weight = w
                selected_edge = (u, v, w)

    if selected_edge is None:
        print("Graph is disconnected. MST is not possible.")
        break

    u, v, w = selected_edge
    visited[u] = True
    visited[v] = True
    mst.append((u, v, w))
    total_cost += w

if len(mst) == n - 1:
    print("\nEdges in Minimum Spanning Tree:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)

    print("Total minimum cost:", total_cost)
