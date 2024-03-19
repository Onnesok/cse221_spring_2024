############################# Task 2 #################################
######################################################################
#Specify path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task2/input1_1.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task2/output1_1.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')
#Read and split
n, m = inp.readline().split(" ")
n = int(n)
m = int(m)
# Defining array size
arr = [[] for i in range (n + 1)]

#Creating list for BFS
for i in range (m):
  x = inp.readline().strip().split()
  # In first nmber of array appending second value
  arr[int(x[0])].append(int(x[1]))
  
#BFS traversal
def BFS(lst, start):
  #Defining queue
  queue = [] 
  #Defining array of n+1
  v = [0]*(int(n) + 1)
  sort = '' #This will be result
  queue.append(start)  #First append start to be able to enter to the loop
  v[start] = 1 #Appended in queue. so do same for array to keep track
  while queue:
      if len(lst[queue[0]]) > 0: 
          for i in range(len(lst[queue[0]])):
              if v[lst[queue[0]][i]] == 0:    #checking
                  queue.append(lst[queue[0]][i])
                  v[lst[queue[0]][i]] = 1
          pop = queue.pop(0) #Now pop
          sort += str(pop) + ' ' #Added space string
      elif len(lst[queue[0]]) <= 0:
          pop = queue.pop(0)
          sort += str(pop) + ' '
  out.write(sort)
  print(sort)


BFS(arr, 1)
out.close()

#Explanation
#First specified path, opened file, readline, converted to int for use, defined array length, created list for bfs traversal. Now wrote a function called BFS, used queue do the operation and v for keeping track of visited edges.
#For answer used a sort string. In the bfs function checked if that value is in queue and v and if not then append. Then after loop do the pop and added to sort string. In the end got the desired output.