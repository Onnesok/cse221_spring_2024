########################################### Task2  ##################################
#####################################################################################
import heapq as hq

def dijkstra(g, s):
    dist = {vertex: float('inf') for vertex in g}
    dist[s] = 0
    q = [(0, s)]
    
    while q:
        current_dist, u = hq.heappop(q)
        if current_dist > dist[u]:
            continue
        for v, w in g[u]:
            alt = current_dist + w
            
            if alt < dist[v]:
                dist[v] = alt
                hq.heappush(q, (alt, v))        
    return dist


#Specify path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab6/task2/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab6/task2/output.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')
#Read and split
n, m = map(int, inp.readline().split())
graph = {i:[] for i in range(n+1)}

for i in range(m):
    u, v, w = map(int, inp.readline().split())
    graph[u].append((v, w))

#starting of alice and bob    
s, t = map(int, inp.readline().split())

#For alice
ds = dijkstra(graph, s)
#For bob
dt = dijkstra(graph, t)

min_time = float('inf')
meet = None
for v in range(1, n+1):
    if ds[v] != float('inf') and dt[v] != float('inf'):
        t = max(ds[v], dt[v])
        if t < min_time:
            min_time = t
            meet = v

if meet == None or min_time == float('inf'):
    out.write("Impossible")
    print("Impossible")
else:
    out.write(f"Time {min_time}\nNode {meet}")
    print(f"Time {min_time}\nNode {meet}")
    
out.close()

#Explanation
#Here specified an input and output file and then opened it in the code and used readline() to read file line by line. In last line ds is for starting node of alice and dt is for starting node of bob. Now passing them in dijkstra algo function
#and got a path list. Now initialize min_time and meet variable and check after the iteration if its same or not. If not then the min_time is Time and meet is Node of the output. Now write them in the file and print output. Done.