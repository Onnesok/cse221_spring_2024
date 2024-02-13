###############################  Task 2 b ################################
##########################################################################

#path declaration
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task2/input2.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task2/output2.txt'


# read the file
inp = open(input_path, 'r')
# generate a output file by running the code
out = open(output_path, 'w')

#Alice
N = int(inp.readline())
array1 = inp.readline().split(" ")
array1 = list(map(int, array1))

#Bob
M = int(f.readline())
array2 = f.readline().split(" ")
array2 = list(map(int, array2))

new = []
p1 = 0
p2 = 0

for i in range(N+M):
  if p1 < N and p2 < M:
    if (array1[p1]) < (array2[p2]):
      new.append(array1[p1])
      p1 += 1
    else:
      new.append(array2[p2])
      p2 += 1

if p2 < M:
  new.extend(array2[p2:])
elif p1 < N:
  new.extend(array2[p1:])

f2.write(" ".join(str(num) for num in new))

f2.close()