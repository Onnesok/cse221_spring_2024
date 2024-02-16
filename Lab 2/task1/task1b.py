#################### Task 1b ###################################
###############################################################

#path declaration
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task1/input1.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task1/output1.txt'

#Reading file
inp = open(input_path, 'r')
#Generating output file
out = open(output_path, 'w')

#Reading line
size, total = map(int, inp.readline().split())  # Reading first line, split and converting to int
numbers = list(map(int, inp.readline().strip().split()))  #Reading second line, stripping for avoiding extra characters in the end and mapping to int after split


left = 0
right = size - 1
flag = False      #Initial flag to check if found
while left<right: 
  current_sum = numbers[left] + numbers[right]
  if current_sum == total: 
    flag = True              #flag changed to save found the number
    break
  elif current_sum < total:     # If less than total then increase from left
    left += 1
  else:                        #Else decrease from right
    right -= 1



if flag == True:
  print(left+1, right+1)
  out.write(f"{left+1} {right+1}")   #Writing on output file
else:
  print("IMPOSSIBLE")
  out.write("IMPOSSIBLE")

out.close()    #Closing output file to save and work properly 

#Explanation
#Here in this problem, I took input from a designated input file, read first line to get size and total sum. Then read second line, stripping for avoiding extra characters in the end and mapping to int after split.
# After that used a while loop and checked if current sum is equal to the given total or not. if equal then flag = true and break. If less than total then increase left index as it's sorted and if greater, then increasing right
#index which we initialized in the begining. After iteration check if flag is true or not. If true then printing output and if still false then the solution is not found. Here we are only using one iteration and so the time
# complexity becomes O(N).