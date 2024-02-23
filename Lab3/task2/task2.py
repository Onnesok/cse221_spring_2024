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
N = int(f.readline())
array1 = f.readline().split(" ")
array1 = list(map(int, array1))

new = array1


def mergeSort(arr):
    res = 0
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
    return res

print(mergeSort(new))
#f2.write(" ".join(str(num) for num in mergeSort(new)))
#print(" ".join(str(num) for num in mergeSort(new)))
f2.close()