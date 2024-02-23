################################## Task 5  ##########################################
#####################################################################################
#Define file location
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task5/input5.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task5/output5.txt'

# read the file
f = open(input_path,"r")
# generate a output file by running the code
f2 = open(output_path,"w")

#Reading input line by line from designated file
n = int(f.readline())  #Reading first line
array1 = f.readline().split(" ")  #Reading second line and spliting
array1 = list(map(int, array1)) #Maping into an array



def quicksort(a, p, r):        # (a,p,r) ~ (array, low, high)
  if p < r:
    q = partition(a, p, r)     # q = pivot index
    quicksort(a, p, q-1)
    quicksort(a, q+1, r)
  return array1

def partition(a, p, r):
  x = a[r]
  i = p-1
  for j in range(p, r, 1):
    if a[j] < x:
      i += 1
      a[i], a[j] = a[j], a[i]
  a[i+1], a[r] = a[r], a[i+1]
  return i+1

# Write Output
f2.write(" ".join(str(num) for num in quicksort(array1, 0, n-1)))    #quicksort(array,low,high)
print(" ".join(str(num) for num in quicksort(array1, 0, n-1)))    #quicksort(array,low,high)

f2.close()  #Closing output file for properly saving

#Explanation
#In this task first specified input and output file path and then opened them. Then read first line, then second line and splited and maped into an array for operations. Here in quicksort() function it takes 3 inputs, which are array, low and high parameter.
# Here q is the pivot index and partition() is the function where we break down the given array into two sub array around pivot element. Then it re-arranges left elements if they are smaller than pivot and for right if they are bigger than pivot. Then it switches i and j. It returns index of the pivot 
#after partitoning in the last for next recursion. Here complexity becomes O(NlogN).