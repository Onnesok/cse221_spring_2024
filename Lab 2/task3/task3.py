###############################  Task 3 ##################################
##########################################################################

#path declaration
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task3/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task3/output.txt'


# read the file
inp = open(input_path, 'r')
# generate a output file by running the code
out = open(output_path, 'w')


size = int(inp.readline())  #Reading array size

print(size)
out.close()         #Closing output file to save and work properly 