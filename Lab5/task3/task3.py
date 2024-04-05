############################# Task 3 #################################
######################################################################
#global
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
f1 = open(input_path, 'r')
f2 = open(output_path, 'w')

n,m = map(int, f1.readline().split())

D = {}
reverseG = {}
for i in range(n+1):
    D[i] = []
    reverseG[i] = []


for i in range(m):
    s,d = map(int, f1.readline().split())
    D[s].append(d)
    #graph with reverse edges
    reverseG[d].append(s)

visited = set()

# topological sort using dfs
for i in range(1,n+1):
    if i not in visited:
        dfs(D, i, visited)

visited.clear()
strong = []
while stack:
    l = []
    x = stack.pop()
    if x not in visited:
        dfs(reverseG,x,visited,TopologicalSortEnabled=False,StrongL=l)

    if l:
        strong.append(l)

#write to file
print(str(strong).strip('[]').replace('], ','\n').replace('[','').replace(']','').replace(',',''))
f2.write(str(strong).strip('[]').replace('], ','\n').replace('[','').replace(']','').replace(',',''))

f1.close()
f2.close()

# step1: Topological Sort
# step2: Reverse the Edges
# step3: Run DFS on reverse edges based on the previously sorted vertex
