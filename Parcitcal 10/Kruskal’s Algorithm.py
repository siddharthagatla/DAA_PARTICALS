# Kruskal's Algorithm using user input
def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]
def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u == root_v:
        return False
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1
    return True
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
edges = []
print("Enter edges as: source destination weight")
for i in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
# Sort edges by weight
edges.sort()
parent = list(range(n))
rank = [0] * n
mst = []
total_cost = 0
for w, u, v in edges:
    if union(parent, rank, u, v):
        mst.append((u, v, w))
        total_cost += w
        if len(mst) == n - 1:
            break
if len(mst) == n - 1:
    print("\nEdges in Minimum Spanning Tree:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)
    print("Total minimum cost:", total_cost)
else:
    print("Graph is disconnected. MST is not possible.")
