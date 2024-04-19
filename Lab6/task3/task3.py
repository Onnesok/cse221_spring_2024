########################################### Task3  ##################################
#####################################################################################
import heapq as hq

def dijkstra(graph, start, end):
    pq = [(0, start)]
    visited = set()
    
    while pq:
        danger, node = hq.heappop(pq)
        if node == end:
            return danger
        
        if node in visited:
            continue
        
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                hq.heappush(pq, (max(danger, weight), neighbor))
    return "Impossible"


#Specify path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab6/task3/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab6/task3/output.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')
#Read and split
n, m = map(int, inp.readline().split())
graph = {i:[] for i in range(n+1)}

for i in range(m):
    u, v, w = map(int, inp.readline().split())
    graph[u].append((v, w))
    
distances = dijkstra(graph, 1, n)

out.write(str(distances))
print(distances)

out.close()

#Explanation
#Here input is taken from specified file and then used readline and got n, m. Now traversed and got u, v and w. Then used dijkstra() function which takes graph, starting node and ending node and return shortest path from start to end.
#In the dijkstra() function I have used priority queue for operation. visited is declared and set() used to populate later. while priority queue is valid pop it and check if the node is end node or not. If not then checked if the node is visited or not 
#and if not visited added to visited to keep track. Now traversing and pushing to queue. As the dijkstras algo returns shortest path and so the ouput will be minimum danger.