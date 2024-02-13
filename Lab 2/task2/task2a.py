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