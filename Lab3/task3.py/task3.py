################################## Task 3  ##########################
#####################################################################################
#Define file location
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task3/input3.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task3/output3.txt'

# read the file
f = open(input_path,"r")
# generate a output file by running the code
f2 = open(output_path,"w")

#Alice
N = int(f.readline())  #Reading first line
array1 = f.readline().split(" ")  #Reading second line and spliting
array1 = list(map(int, array1)) #Maping into an array

new = array1

#Merge sort
def mergeSort(arr):
    res = 0             #Flag where max value will be saved and returned
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0


        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                res = R[j]
                i += 1
            else:
                res = L[i]
                j += 1
            k += 1

        while i > len(L):
            res = L[i]
            i += 1
            k += 1
        while j > len(R):
            res = R[j]
            j += 1
            k += 1
            
    else:
        res = arr[0]
    return res

print(mergeSort(new))
f2.write(str(mergeSort(new)))
f2.close()