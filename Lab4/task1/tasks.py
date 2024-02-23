############################# Task 1 #################################
######################################################################

input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task1/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task1/output.txt'
 
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




############################################################################
#############################################################################

# file_in = open("/content/sample_data/input1b.txt","r")
# file_out = open("/content/sample_data/output1b.txt","w")

# nodes, edges = file_in.readline().split(" ")
# nodes = int(nodes)
# edges = int(edges)
# arr = [[] for i in range (nodes+1)]
# # print(arr, nodes)
# for i in range (edges):
#   u,v,w = file_in.readline().split(" ")
#   # print(u,v,w)
#   u = int(u)
#   v = int(v)
#   w = int(w)
#   tup1 = (v,w)
#   arr[u].append(tup1)
#   # print(arr)
# for i in range(len(arr)):
#   print(str(i),end=": ")
#   file_out.write(f"{i}: ")
#   for j in range(len(arr[i])):
#     print(arr[i][j],end = " ")
#     file_out.write(f"{arr[i][j]} ")
#   print()
#   file_out.write(f"\n")

#   # file_out.write(f"{i} : \n")
# file_in.close()
# file_out.close()