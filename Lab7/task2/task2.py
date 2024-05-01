def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal(N, edges):
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    edges.sort(key=lambda x: x[2])
    mst_cost = 0
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_cost += w
    return mst_cost

# Input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# Output
print(kruskal(N, edges))