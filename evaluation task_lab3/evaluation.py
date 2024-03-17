###################################  Colab files  ####################################
######################################################################################

################################## Evaluation Task  ##################################
#####################################################################################

# read the file
f = open("input2.txt","r")
# generate a output file by running the code
f2 = open("output2.txt","w")

#Alice
N = int(f.readline())
array1 = f.readline().split(" ")
array1 = list(map(int, array1))

# Bob
M = int(f.readline())
array2 = f.readline().split(" ")
array2 = list(map(int, array2))

#Trudy
L = int(f.readline())
array3 = f.readline().split(" ")
array3 = list(map(int, array3))

new = array1 + array2 + array3

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

#f2.write(" ".join(str(num) for num in mergeSort(new)))
print(" ".join(str(num) for num in mergeSort(new)))
f2.close()

