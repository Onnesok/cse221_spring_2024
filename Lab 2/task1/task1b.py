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











# # Reading input
# N, S = map(int, input().split())
# numbers = list(map(int, input().split()))

# # Two-pointer approach to find indices with the given sum
# left, right = 0, N - 1
# found = False
# while left < right:
#     current_sum = numbers[left] + numbers[right]
#     if current_sum == S:
#         found = True
#         break
#     elif current_sum < S:
#         left += 1
#     else:
#         right -= 1

# # Printing result
# if found:
#     print(left + 1, right + 1)  # Adjust indices to 1-based indexing
# else:
#     print("IMPOSSIBLE")