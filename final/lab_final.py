########################################### Lab final  ##################################
#####################################################################################
import heapq

def max_probability(N, M, edges, start, end):
    graph = {i: [] for i in range(N)}
    for u, v, p in edges:
        graph[u].append((v, p))
        graph[v].append((u, p))

    pq = [(-1.0, start)]
    visited = set()

    while pq:
        prob, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        if node == end:
            return -prob

        for neighbor, edge_prob in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (prob * edge_prob, neighbor))

    return 0.0



input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/final/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/final/output.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')

# Input
N, M = map(int, inp.readline().split())
edges = [list(map(float, inp.readline().split())) for _ in range(M)]
# print(edges)
start, end = map(int, inp.readline().split())

# Output
result = max_probability(N, M, edges, start, end)
print(result)
out.write(str(result))
out.close()


















