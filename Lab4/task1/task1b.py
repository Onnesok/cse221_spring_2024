############################# Task 1B #################################
######################################################################

input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task1/input1_1.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task1/output1_1.txt'
 
inp = open(input_path, 'r')
out = open(output_path, 'w')



nodes, edges = inp.readline().split(" ")
nodes = int(nodes)
edges = int(edges)
arr = [[] for i in range (nodes + 1)]
for i in range (edges):
  u,v,w = inp.readline().split(" ")
  u = int(u)
  v = int(v)
  w = int(w)
  tupl = (v, w)
  arr[u].append(tupl) 
for i in range(len(arr)):
  out.write(str(i)+":"+ ', '.join([f"({t[0]}, {t[1]})" for t in arr[i]]) + "\n")
  print(str(i) +":"+ ', '.join([f"({t[0]}, {t[1]})" for t in arr[i]]))  # as for .joint function we need string so converted to string

out.close()
