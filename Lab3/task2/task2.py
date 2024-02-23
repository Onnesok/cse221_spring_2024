################################## Task 2  ##########################
#####################################################################################
#Define file location
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task2/input2.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task2/output2.txt'

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
    if len(arr) > 1:    #if array size > 1
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
            
    else:                    #if array size is 1 and nothing to compare and merge
        res = arr[0]
    return res

print(mergeSort(new))
f2.write(str(mergeSort(new)))    #Writing output
f2.close()  #Closing file to work properly

#Explanation
#In this code first I have defined the file location, opened them in the code, read first line and then converted second line to an array for next operation. Then wrote a merge sort algorithm to
#compare or get the max value. So initiated a flag called res and checked if the array size is greater than 1 or not. if not then thats the max and if there is other values then divided array to half and
#merged process to get the max value. Lastly returned res and printed and closed the file. Here the time complexity is O(NlogN).