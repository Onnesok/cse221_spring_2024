############################# Task 1A #################################
######################################################################

input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task1/input1_1.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task1/output1_1.txt'
 
inp = open(input_path, 'r')
out = open(output_path, 'w')



nodes, edges = inp.readline().split(" ")
nodes = int(nodes)
edges = int(edges)
arr = [[0]*(nodes+1) for i in range (nodes+1)]
for i in range (edges):
  u,v,w = inp.readline().split(" ")
  u = int(u)
  v = int(v)
  w = int(w)
  arr[u][v] = w
for i in arr:
  out.write(f"{i} \n")
  print(f"{i} \n")

out.close()


