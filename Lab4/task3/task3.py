############################# Task 2 #################################
######################################################################

#Specify path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task3/input1_1.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task3/output1_1.txt'
#OPen file
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
    arr[int(v)].append(int(u))
  
#print(arr)
def DFS(g, start):
    chk = []                # For checking stack
    stack = [start]         # stack
    res = ''                  # Main result string
    while stack:              # If stack not empty loop will work
        node = stack.pop()      # pop first and check if already exist in chk
        if node not in chk:
            res += str(node) + ' '      # If dont then thats one vertex
            chk.append(node)            # Insert to chk to keep track that we've used it
            stack.extend(reversed(g[node]))     # we need reverse value, so reversed and extended to array
    out.write(res)      
    print(res)
    
DFS(arr, 1)
out.close()
