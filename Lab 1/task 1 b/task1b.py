##################### Task 1b  #####################
###################################################

#Reading file
inp2 = open('input1b.txt', 'r')
#Generating output file
out2 = open('output1b.txt', 'w')

#Reading line
line = int(inp2.readline())

for i in range(0, line):
  n = inp2.readline()                             #Reading every line using loop
  lekha = n.split("+")                            #Spliting from + sign
  if "+" in n:             
    temp = n.split("+")                           #Spliting from + sign
    temp1 = temp[0].split(" ")                    #Spliting from space
    res = int(temp1[1]) + int(temp[1])            #Convert to int and sum up
    
    #print(f"The result of {int(temp1[1])} + {int(temp[1])} is {res}")
    #Writing in output file
    out2.write(f"The result of {int(temp1[1])} + {int(temp[1])} is {res}\n")  
    
  elif "*" in n:
    temp = n.split("*")                           #Spliting from * sign
    temp1 = temp[0].split(" ")                    #Spliting from space
    res = int(temp1[1]) * int(temp[1])            #Result
    
    #print(f"The result of {int(temp1[1])} * {int(temp[1])} is {res}")
    #Writing output file
    out2.write(f"The result of {int(temp1[1])} * {int(temp[1])} is {res}\n")  
    
    
  elif "-" in n:
    temp = n.split("-")                     #Spliting from - sign
    temp1 = temp[0].split(" ")              #Spliting from space
    res = int(temp1[1]) - int(temp[1])
    #print(f"The result of {int(temp1[1])} - {int(temp[1])} is {res}")
    #Writing output file
    out2.write(f"The result of {int(temp1[1])} - {int(temp[1])} is {res}\n")
    
    
  elif "/" in n:
    temp = n.split("/")                       #Spliting from / sign
    temp1 = temp[0].split(" ")                #Spliting from space
    res = int(temp1[1]) / int(temp[1])
    #print(f"The result of {int(temp1[1])} + {int(temp[1])} is {res}")
    #Writing output file
    out2.write(f"The result of {int(temp1[1])} / {int(temp[1])} is {res}\n")
    
out2.close()
###Explanation
# Here input and output file is being loaded and sliced depending on the sign. signs are +,-,*,/. then again sliced when got space.
#By this way we're getting two string and then converting them to int. Then did the respective operation.
    