def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, size, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if size[root_x] < size[root_y]:
            root_x, root_y = root_y, root_x
        parent[root_y] = root_x
        size[root_x] += size[root_y]
        return size[root_x]
    return size[root_x]

def friend_circle_size(N, K, queries):
    parent = [i for i in range(N)]
    size = [1] * N
    result = []
    for query in queries:
        A, B = query
        result.append(union(parent, size, A - 1, B - 1))
    return result



#Specify input file path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab7/task1/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab7/task1/output.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')

# Reading input
N, K = map(int, inp.readline().split())

queries = [list(map(int, inp.readline().split())) for i in range(K)]

# Output
for size in friend_circle_size(N, K, queries):
    print(size)
    out.write(f"{str(size)}\n")
    
    
out.close()    
    

#Explanation
# Here I am taking input from a specified file location, reading and spliting and saving in variables. Then, iterate and sending N, K and queries to friend_circle_size() function where it returns results. In friend_circle_size() function, I am initializing arrays for operations and doing query operations.
# Unpacked A, B and  sending to union() function to merge disjoint sets. And from union() to find root of the set sending data to find() function. Here, I have used multiple functions to increase usablity.
# In the end printing and saving output and out.close() for safely saving output.