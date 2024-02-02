##################### Task 2  #####################
####################################################

#Bubble  sort code as function
def bubbleSort(arr):
  swapped = False       # Took a flag and initialized as false
  for i in range(len(arr)-1):
    swapped = False
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True                # If the loop comes here that means it's not sorted and swaping

    if swapped == False:              # If array is sorted then swapped = false
      break
  return arr


f = open("input2.txt","r")   # read the file

f2 = open("output2.txt","w")  # Generate output file


arr_size = int(f.readline())     # reading array size


array = f.readline().split(" ")  # spliting array

array = list(map(int, array))   # Convert ['1','2'] to [1,2]

f2.write(" ".join(str(num) for num in bubbleSort(array)))  # Now joining them to get [1 2 3 4 5]
f2.close()  # closing file for safety

###Explanation
# Here input and output file is being loaded and determining size or reading size given on the first line using readline()
#Then we're converting to respective array format and sending data to bubblesort() function. Inside the function I took a flag 
# to keep track if data is sorted or not to optimize sorting. If data is sorted then no need to perform bubble sort and swapped = false will be the value
# Else sort operation will be performed and as the loop will enter in nested loops so swapped = true will be the value that time.