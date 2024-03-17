############################# Task 2 #################################
######################################################################

input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task2/input1_1.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task2/output1_1.txt'
 
inp = open(input_path, 'r')
out = open(output_path, 'w')



n, m = inp.readline().split(" ")
n = int(n)
m = int(m)
arr = [[] for i in range (n + 1)]

for i in range (m):
  x = inp.readline().strip().split()
  arr[int(x[0])].append(int(x[1]))
  
  
def BFS(lst, start):
  queue = []
  v = [0]*(int(n) + 1)
  sort = ''
  queue.append(start)
  v[start] = 1
  while queue:
      if len(lst[queue[0]]) > 0:
          for i in range(len(lst[queue[0]])):
              if v[lst[queue[0]][i]] == 0:
                  queue.append(lst[queue[0]][i])
                  v[lst[queue[0]][i]] = 1
          pop = queue.pop(0)
          sort += str(pop) + ' '
      elif len(lst[queue[0]]) <= 0:
          pop = queue.pop(0)
          sort += str(pop) + ' '
  out.write(sort)
  print(sort)


BFS(arr, 1)
out.close()


# Check with last sample :)