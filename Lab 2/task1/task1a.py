#################### Task 1a ###################################
###############################################################
#path declaration
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task1/input1.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task1/output1.txt'

#Reading file
inp = open(input_path, 'r')
#Generating output file
out = open(output_path, 'w')

#Reading line
firstline = inp.readline().split()
line2 = inp.readline().strip().split()  #strip for avoiding extra space in the end


size = int(firstline[0])  #size of the array
total = int(firstline[1]) 

flag = False      #Initializing a flag to see if the condition is satisfied
for i in range(size):
    for j in range(i+1, size):
        if (int(line2[i]) + int(line2[j]) == total):
            idx1 = i+1
            idx2 = j+1
            out.write(str(idx1) + " "+ str(idx2))  #Writing result on output file
            print(idx1, idx2)           # printing index
            flag = True                 # Make flag= True to indicate that the condition satisfies
            break                       # Break to avoid more iteration
    if (flag == True):                  # For multiple possiblities if flag is true or found one then break to only print one answer
        break

if flag == False:                     # Flag = false means no solution found as per condition
  out.write("IMPOSSIBLE")
  print("IMPOSSIBLE")

out.close()    #Closing output file to save and work properly 

#Explanation
#Here in this problem, I took input from a designated input file, read first line to get the size and sum of the number. Initialized a flag to keep track if the value is found or not.
#Then used a nested loop and checked if values sum == total. if it matches then index will be i+1 and j+1. Then wrote it to output file and also printed them. Then mmade the flag = True to 
# keep track that the value is found and break the iteration. As we dont need multiple answers and so if the flag=true then the loop will break and no more work is needed. But in the end if it is false
#that means that the value is not found. Closing the output file in the last to save them properly. Here the solution is O(N^2) as the iteration is nested