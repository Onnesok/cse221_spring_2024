############################# Task 4 #################################
######################################################################

#Specify path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task4/input1_1.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task4/output1_1.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')
#Read and split
n, m = inp.readline().split(" ")
n = int(n)
m = int(m)
# Define array size
arr = [[] for i in range (n + 1)]
#Create list for dfs
for i in range (m):
    u, v = inp.readline().strip().split(' ')
    arr[int(u)].append(int(v))

print(arr)

def DFS(g, start, visited, stack):
    visited[start] = True
    stack[start] = True
    for neighbor in g[start]:
        if not visited[neighbor]:
            if DFS(g, neighbor, visited, stack):
                return True
        elif stack[neighbor]:
            return True

    stack[start] = False
    return False

def hasCycle(g):
    visited = [False] * (n + 1)
    stack = [False] * (n + 1)

    for node in range(1, n + 1):
        if not visited[node]:
            if DFS(g, node, visited, stack):
                return True
    return False

if hasCycle(arr):
    out.write("YES")
    print("YES")
else:
    out.write("NO")
    print("NO")

out.close()



##### ki hoise bujhi nai
