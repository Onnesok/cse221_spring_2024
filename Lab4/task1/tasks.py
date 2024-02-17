############################# Task 1 #################################
######################################################################

input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task1/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task1/output.txt'
 
inp = open(input_path, 'r')
out = open(output_path, 'w')

#print(content)
firstline = inp.readline()
s = inp.readline()

print(firstline, s)

out.close()