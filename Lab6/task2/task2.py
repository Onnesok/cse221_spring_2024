########################################### Task2  ##################################
#####################################################################################
import math
import heapq as hq

def dijkstra(dc, s):
    dist = [math.inf]*len(dc)
    dist[s] = 0
    q = []
    hq.heappush(q, (dist[s], s))
    prev = [None]*len(dc)
    visited = [False]*len(dc)
    cost = 0
    
    while q:
        num, u = hq.heappop(q)
        if visited[u] == True:
            continue
        visited[u] = True
        for v, cost in dc[u]:
            alt = dist[u] + cost
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                hq.heappush(q, (dist[v], v))
                
    dist.pop(0)
    while math.inf in dist:
        idx = dist.index(math.inf)
        dist[idx] = -1
    return dist

#Specify path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab6/task2/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab6/task2/output.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')
#Reading all input at once and slicing it
inp = inp.read().split("\n")
line1 = inp[0].split(" ")

nodes = int(line1[0])
edges = int(line1[1])
source = int(inp[-1])

dc = {i:[] for i in range(nodes+1)}

for i in range(1, edges+1, 1):
    info = inp[i].split(" ")
    node1 = int(info[0])
    node2 = int(info[1])
    cost = int(info[2])
    arr = dc[node1]
    arr.append((node2, cost))
    
costs = dijkstra(dc, source)
out.write(" ".join(map(str, costs)))
print(" ".join(map(str, costs)))

out.close()  #closing for safely saving

#Explanation
#Here input is taken from a specified file and read() is used to read files all at once and then sliced and got the n, m and source. Now created a dictonary and populated those with the values of nodes and costs.
#Now dijkstra() algorithm is used to determine shortest path. In the dijkstra() function it takes dc and source. It returns list of shortest distance from the source to every nodes. Now print the list after slicing and joining
#using .join() and we got our answer.