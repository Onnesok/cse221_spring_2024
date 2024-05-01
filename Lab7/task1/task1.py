def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, size, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if size[root_x] < size[root_y]:
            root_x, root_y = root_y, root_x
        parent[root_y] = root_x
        size[root_x] += size[root_y]
        return size[root_x]
    return size[root_x]

def friend_circle_size(N, K, queries):
    parent = [i for i in range(N)]
    size = [1] * N
    result = []
    for query in queries:
        A, B = query
        result.append(union(parent, size, A - 1, B - 1))
    return result

# Input
N, K = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(K)]

# Output
for size in friend_circle_size(N, K, queries):
    print(size)