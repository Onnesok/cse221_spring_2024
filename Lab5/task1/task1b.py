############################# Task 1A #################################
######################################################################
#Using BFS approach

#Specify path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab5/task1/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab5/task1/output.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')

#global
result = []
queue = []

def bfs(G, v, visited, Indeg):
    visited.add(v)
    queue.append(v)

    while queue:
        x = queue.pop(0)
        result.append(x)

        for neighbour in G[x]:
            # reduce child indeg by 1
            Indeg[neighbour] -= 1

            if neighbour not in visited and Indeg[neighbour] == 0:
                visited.add(neighbour)
                queue.append(neighbour)
            
            
#Reading nodes and edges using readline and splitting
n,m = map(int, inp.readline().split())
arr = [[]*(n+1) for i in range (n+1)]
InDeg = [0]*(n+1)

for i in range(m):
    A,B = map(int, inp.readline().split())
    arr[A].append(B)
    InDeg[B] += 1
    
#Empty set for populating with unique nodes    
visited = set()


for i in range(1,n+1):
    if InDeg[i] == 0 and i not in visited:
        bfs(arr, i, visited, InDeg)

# if it fails to visit all nodes/vertex.
if len(result) < n:
    print("IMPOSSIBLE")
    out.write('IMPOSSIBLE')
else:
    # print list to output format
    print(str(result).strip('[]').replace(',',''))
    out.write(str(result).strip('[]').replace(',',''))


inp.close() #Closing for safety
out.close() #Closing for safely saving

#Explanation
# Here took input from file by specifying path, opened file, split and got n, m. Also there is a global variable result[] array to store result. Used this global variable for static charactristic.
#First took empty array of n+1 length and indeg. Then reading A, B and appending in array and indeg. Visited is empty set and here iterating through each nodes with in degree 0 and not visited before.
# Now bfs is checking if every node is visited or not and indeg of neighbor is 0. If every node is visited then we got the anser and else it's not possible.
