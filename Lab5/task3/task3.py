############################# Task 3 #################################
######################################################################
#global stack
stack = []

def dfs(G, v, visited, TopologicalSortEnabled=True, StrongL = None):
    visited.add(v)
    if not TopologicalSortEnabled:
        StrongL.append(v)

    for neighbour in G[v]:
        if neighbour not in visited:
            dfs(G, neighbour, visited, TopologicalSortEnabled, StrongL)

    if TopologicalSortEnabled:
        stack.append(v)


input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab5/task3/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab5/task3/output.txt'
inp = open(input_path, 'r')
out = open(output_path, 'w')

n,m = map(int, inp.readline().split())

D = {}
reverseG = {}
for i in range(n+1):
    D[i] = []
    reverseG[i] = []


for i in range(m):
    s,d = map(int, inp.readline().split())
    D[s].append(d)
    #graph with reverse edges
    reverseG[d].append(s)

visited = set()

# topological sort using dfs
for i in range(1,n+1):
    if i not in visited:
        dfs(D, i, visited)

# Clear visited set for next traversal
visited.clear()
# List to store strongly connected components
strong = []

# Traverse stack to find strongly connected components
while stack:
    l = []
    x = stack.pop()
    if x not in visited:
        dfs(reverseG,x,visited,TopologicalSortEnabled=False,StrongL=l)

    if l:
        strong.append(l)

#write to file
print(str(strong).strip('[]').replace('], ','\n').replace('[','').replace(']','').replace(',',''))
out.write(str(strong).strip('[]').replace('], ','\n').replace('[','').replace(']','').replace(',',''))

inp.close()
out.close()

#Explanation
# First doing Topological Sort. Next, Reverse the Edges. Now, Run DFS on reverse edges based on the previously sorted vertex. Here, taking input from file, spliting to n, m. Initialize empty dictionary for adjacency liist and reverseG = {} for reverse graph. Now populate them. Next, Populate graph and its reverse with edges from input file.
#visited to keep track of visited. Next topological sort using dfs. Traverse stack to find strongly connected components. Now print and write in output. Closing file for safely saving.
