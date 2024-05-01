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




#Specify input file path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab7/task2/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab7/task2/output.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')

# Reading input
N, M = map(int, inp.readline().split())

edges = [list(map(int, inp.readline().split())) for _ in range(M)]

# Output
print(kruskal(N, edges))
out.write(str(kruskal(N, edges)))

#Explanation
#Here took input from a specified path and split and sent to kruskal() function. It takes N which is number of cities and edges. Inside function initialized parents and rank and sorted edges based on their maintainance costs in ascending order.
#Then if u and v is not in the same set, they are united using union() function. This is continuing until all the cities are connected in a single MST. Lastly, mst_cost is returned and print and also write in output file. out.close() for safely saving.