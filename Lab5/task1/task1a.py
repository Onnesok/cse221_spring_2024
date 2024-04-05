############################# Task 1A #################################
######################################################################
#Using DFS approach

#Specify path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab5/task1/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab5/task1/output.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')

#global
result = []

#DFS
def dfs(G, v, visited, Indeg):
    visited.add(v)
    result.append(v)

    for neighbour in G[v]:
        #set the inDeg of child nodes --1
        Indeg[neighbour] -= 1

        if neighbour not in visited and Indeg[neighbour] == 0:
            dfs(G, neighbour, visited, Indeg)
            
            
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
        dfs(arr, i, visited, InDeg)

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
#First took empty array of n+1 length and indeg. Then reading A, B and appending in array and indeg. Visited is empty set and here iterating through each nodes with in degree 0 and not visited before. Dfs 
#function is used recursively here . Dfs function conducts traversal recursively, visiting neighbors of a given vertex while decrementing their in-degree. It ensures traversal only to unvisited neighbors with
# an in-degree of 0. Now if no node is left unvisited or every node is visited then We got the result. Else impossible and writing to output.







