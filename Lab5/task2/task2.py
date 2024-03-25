import heapq

#global
result = []
priority_queue = []
heapq.heapify(priority_queue)

def bfs(G, v, visited, Indeg):
    visited.add(v)
    heapq.heappush(priority_queue,v)

    while priority_queue:
        x = heapq.heappop(priority_queue)
        result.append(x)

        for neighbour in G[x]:
            # reduce child indeg by 1
            Indeg[neighbour] -= 1

            if neighbour not in visited and Indeg[neighbour] == 0:
                visited.add(neighbour)
                heapq.heappush(priority_queue,neighbour)

input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab5/task2/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab5/task2/output.txt'
f1 = open(input_path, 'r')
f2 = open(output_path, 'w')

n,m = map(int, f1.readline().split())

D = {}
for i in range(n+1):
    D[i] = []

InDeg = [0]*(n+1)
for i in range(m):
    s,d = map(int, f1.readline().split())
    D[s].append(d)
    InDeg[d] += 1

visited = set()

for i in range(1,n+1):
    if InDeg[i] == 0 and i not in visited:
        bfs(D, i, visited, InDeg)

# if it fails to visit all nodes/ver.
if len(result) < n:
    print('IMPOSSIBLE',end='',file=f2)
else:
    # print list to output format
    print(str(result).strip('[]').replace(',',''))
    f2.write(str(result).strip('[]').replace(',',''))

f1.close()
f2.close()