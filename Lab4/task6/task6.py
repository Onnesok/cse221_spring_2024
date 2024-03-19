############################# Task 6 #################################
######################################################################
from collections import deque

#Specify path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task6/input1_1.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task6/output1_1.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')
#Read and split
n, m, d = inp.readline().strip('\n').split(' ')
#Creating adjacency list of (n+1)
adjls = [[] for i in range(int(n)+1)]

#BFS traversal
def BFS(graph, start, end):
    #Used queue as its bfs
    queue = deque([(start, [start])])
    visited = [False] * (len(graph)+1) #visited array for keeping track
    visited[start] = True
    while queue:
        node, p = queue.popleft()
        if node == end:  #when found destination returning path
            return p

        for ng in graph[node]:
            if not visited[ng]:
                visited[ng] = True
                queue.append((ng, p + [ng]))
    return []

#Creating adjacent list for bfs input
for i in range(int(m)):
  u, v = inp.readline().strip('\n').split(' ')
  adjls[int(u)].append(int(v))
  adjls[int(v)].append(int(u))

#Here p is the path
p = BFS(adjls, 1, int(d))
s = ''
#converting p to string adding for desired output format
for i in p:
  s+=str(i)+' '

if p:
    #printing time and path
    print(f'Time: {len(p)-1}\nShortest Path: {s}')
    out.write(f'Time: {len(p)-1}\nShortest Path: {s}')


out.close()  #closing output file for safety and saving without delay

#Explanation
# Took input from a file, splited and got n, m and d. Now created adjacency list and bfs function. In last part of the code iterated and created adjls for iteration and called bfs function where adjacency list , start and destination is given.
#In bfs function While the queue is not empty, it dequeues a node and its path and if node is found then returns path. Else it iterates through the adjacent nodes and keeps adding unvisited neighbors to the queue with the updated path and marks them as visited.
#Last part converted path to string and if p is not null printed time and path.



