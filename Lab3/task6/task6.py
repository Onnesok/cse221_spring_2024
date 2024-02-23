################################## Task 6  ##########################################
#####################################################################################

def k_smallest(arr,l,h,k):
  if l<=h:  # Base case
    pivot = arr[h]
    i = l-1
    for j in range(l,h):
      if arr[j]<= pivot:            #checking arr[j] is less or eqaul to pivot
        i+=1
        arr[i],arr[j] = arr[j],arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    p = i+1
    if p+1==k:                  #Checking if the pivot is the k-th smallest element
      return arr[p]
    elif p+1<k:
      return k_smallest(arr,p+1,h,k)                # If k is in the right sub-array, recursively search the right
    else:
      return k_smallest(arr,l,p-1,k)                #If k is in the left sub-array, recursively search the left
  

#Define file location
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task6/input6.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task6/output6.txt'

# read the file
f = open(input_path,"r")
# generate a output file by running the code
f2 = open(output_path,"w")


N = int(f.readline().strip())                           #Reading first line
array = list(map(int,f.readline().strip().split()))     # Mapping array
q = int(f.readline().strip())                           #number of queries


#Reading query elements
for i in range(q):                                      
  K = int(f.readline().strip())
  result = k_smallest(array, 0, len(array)-1, K)
  print(result)
  f2.write(str(f"{result}\n"))
  
f2.close()   #For properly saving

#Here in this Code I used quick sort without partition function to find kth smallest value. First took input from designated file and read elements line by line using readline(). Then called the function where
#k_smallest function takes an array arr, and indices l (low) and h (high),along with the order statistic k. The time complexity here is O(NlogN).