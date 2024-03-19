############################# Task 1B #################################
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
#Define an array of (nodes + 1) but now empty for adjacency list
arr = [[] for i in range (nodes + 1)]
for i in range (edges):
  #Reading u, v, w
  u,v,w = inp.readline().split(" ")
  u = int(u)
  v = int(v)
  w = int(w)
  tupl = (v, w)
  # appending tuple to u position of the array
  arr[u].append(tupl)
for i in range(len(arr)):
  #writing to file
  out.write(str(i)+":"+ ', '.join([f"({t[0]}, {t[1]})" for t in arr[i]]) + "\n")
  print(str(i) +":"+ ', '.join([f"({t[0]}, {t[1]})" for t in arr[i]]))  # as for .joint function we need string so converted to string

out.close()  #Closing for safely saving



#Explanation
# Here first I specified path and opened it, read first line and converted to int for operation. Now creating (nodes + 1) length of empty array. In the u position of the array placing tuple.
#For writing output in desired way I need a single string. So summed up the string in the iteration. For tuple used join function to print just value.