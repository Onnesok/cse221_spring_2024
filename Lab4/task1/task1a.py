############################# Task 1A #################################
######################################################################
#Specify path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task1/input1_1.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task1/output1_1.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')


#Reading nodes and edges using readline and splitting
nodes, edges = inp.readline().split(" ")
#I need int and so convert int from string
nodes = int(nodes)
edges = int(edges)
#Define a 2d array of (nodes + 1)
arr = [[0]*(nodes+1) for i in range (nodes+1)]
for i in range (edges):
  #Reading u, v, w
  u,v,w = inp.readline().split(" ")
  u = int(u)
  v = int(v)
  w = int(w)
  arr[u][v] = w #placing values
for i in arr:
  #writing to file
  out.write(f"{i} \n")
  print(f"{i} \n")

out.close() #Closing for safely saving

#Explanation
# Here first I specified path and opened it, read first line and converted to int for operation. Now creating (nodes + 1) length of 2d array and placing the value
#So we got the answer or output


