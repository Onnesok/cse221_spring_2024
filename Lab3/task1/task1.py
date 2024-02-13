############################# Task 1 #################################
######################################################################

input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task1/input1.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task1/output1.txt'
 
inp1 = open(input_path, 'r')
#out1 = open(output_path, 'w')

#print(content)
firstline = inp1.readline()
s = inp1.readline()

print(firstline, s)
