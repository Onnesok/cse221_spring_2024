##################### Task 1a  #####################
###################################################

#Reading file
inp = open('input1a.txt', 'r')
#Output file generation
out = open('output1a.txt', 'w')

#Reading line
line = int(inp.readline())

for i in range(0, line):
    n = int(inp.readline())  #Reading every line using loop
    
    if n%2 == 0:                #even
        out.write(f"{n} is an Even number\n")  #Writing output
        #print(f"{n} is even\n")
    else:                       #Odd
        out.write(f"{n} is an Odd number\n")   #Writing output
        #print(f"{n} is odd\n")
        
out.close()

###Explanation
# Here input and output file is being loaded and checked if number is even or odd. File is being read using readline() which reads line by line.
#After that result is being written in output file using out.write