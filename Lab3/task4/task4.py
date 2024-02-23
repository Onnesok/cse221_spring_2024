################################## Task 4  ##########################################
#####################################################################################
#Define file location
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task4/input4.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task4/output4.txt'

# read the file
f = open(input_path,"r")
# generate a output file by running the code
f2 = open(output_path,"w")

#Reading input line by line from designated file
N = int(f.readline())  #Reading first line
array1 = f.readline().split(" ")  #Reading second line and spliting
array1 = list(map(int, array1)) #Maping into an array



max_val=float("-inf")       #max_val is set to lowest value
def merge(arr1,arr2):
  global max_val            #global variable for always access
  i,j=1,1                   # i, j initialization
  
  while i<len(arr1)+1:
    if j<len(arr2)+1:
      if (arr1[i-1] + (arr2[j-1])**2)>max_val:       #check if its greater than max_val or not
        max_val=arr1[i-1] + (arr2[j-1])**2
      j+=1
    elif j==len(arr2)+1:
      j=0
      i+=1 
  return arr1+arr2



#Merge sort function
def mergesort(arr):
    if len(arr) > 1:   #check if there is next element to compare
        mid = len(arr) // 2
        l = mergesort(arr[:mid])
        r = mergesort(arr[mid:])
        return merge(l, r)
    else:                      # If size is 1 then nothing to do
        return arr


result = mergesort(array1)
f2.write(str(max_val))
print(max_val)


#Explanation
#In this task first specified input and output file path and then opened them. Then read first line, then second line and splited and maped into an array for operations. There is 2 functions in this code.
# mergesort() function takes array input and splits them like usual greedy approach and also checks if the array is 1 sized or greater than that. if array is greater than 1 then it sends left and right side of the 
#array to another merge() function to find maximum. In the merge() function a gloabal function is declared to keep  track of the maximum value and in the last part the merge() function returns the summed up array it received
# and the rest is continued. Complexity of this code is O(NlogN)