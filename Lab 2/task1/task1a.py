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