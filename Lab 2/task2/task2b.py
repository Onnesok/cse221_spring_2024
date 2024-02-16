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
N = int(inp.readline())  #Reading array size
array1 = inp.readline().split(" ")  # Reading array and spliting from space
array1 = list(map(int, array1))     #Converting string to int and then list or array

#Bob
M = int(inp.readline())               #Reading array size
array2 = inp.readline().split(" ")    # Reading array and spliting from space
array2 = list(map(int, array2))     #Converting string to int and then list or array

new = []      #Empty list to store new sorted array
p1 = 0
p2 = 0

for i in range(N+M):
  if p1 < N and p2 < M:
    if (array1[p1]) < (array2[p2]):
      new.append(array1[p1])      #Small value gets added to the new list
      p1 += 1                     
    else:
      new.append(array2[p2])      #Else add whatever we have
      p2 += 1

#Check and add if any value is left behind
if p2 < M:
  new.extend(array2[p2:])
elif p1 < N:
  new.extend(array2[p1:])

out.write(" ".join(str(num) for num in new))  #Writing on output file
print(" ".join(str(num) for num in new))      #Printing result

out.close()         #Closing output file to save and work properly 


#Explanation
#Here in this problem, I took input from a designated input file, read first line to get the size of the array of alice. Then in second line converted to int and made a array from them. I did the same thing for bob too.
#After that I have summed up those arrays to create a new array. Then used a loop of n+m size and checked which value is smaller. Small value is added to the new list. Then also extended to check if any value is left behind.
# Then printed and wrote output. Here as there is just one loop or iteration so here the time complexity is O(n).