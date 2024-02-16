###############################  Task 2 a ################################
##########################################################################

#path declaration
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task2/input2.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task2/output2.txt'


# read the file
inp = open(input_path, 'r')
# generate a output file by running the code
out = open(output_path, 'w')

#Alice
N = int(inp.readline())  # Reading array size
array1 = inp.readline().split(" ")  # Reading array and spliting from space
array1 = list(map(int, array1))     #Converting string to int and then list or array

# Bob
M = int(inp.readline())         # Reading array size
array2 = inp.readline().split(" ")      # Reading array and spliting from space
array2 = list(map(int, array2))         #Converting string to int and then list or array

new = array1 + array2                   #Summing up arrays

#Merge sort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0


        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

out.write(" ".join(str(num) for num in mergeSort(new)))  #Writing on output file
print(" ".join(str(num) for num in mergeSort(new)))      #Printing result
out.close()    #Closing output file to save and work properly 

#Explanation
#Here in this problem, I took input from a designated input file, read first line to get the size of the array of alice. Then in second line converted to int and made a array from them. I did the same thing for bob too.
#After that I have summed up those arrays to create a new array. Then wrote merge sort function to sort the unsorted new summed up array. merge sort is used cause it's time complexity is O(nlogn). It works by dividing array
#in 2 parts and sorting them. After that wrote the output in output file and also printed it. out.close() for properly closing the output file and saving properly.