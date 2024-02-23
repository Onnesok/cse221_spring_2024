################################## Task 1 ##################################
#####################################################################################

#Define file location
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task1/input1.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task1/output1.txt'


# read the file
f = open(input_path,"r")
# generate a output file by running the code
f2 = open(output_path,"w")

#Alice
N = int(f.readline())  #Reading first line
array1 = f.readline().split(" ")  #Reading second line
array1 = list(map(int, array1))   #maping into an array

new = array1

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

f2.write(" ".join(str(num) for num in mergeSort(new)))  #Writing output to file
print(" ".join(str(num) for num in mergeSort(new))) 
f2.close()  #Closing file to save and work properly



#Explanation
#In this code I have specified input and output file location and opened them in code. Then read array of alice and wrote a merge sort function. The merge sort function works here by deviding array in half
#and merging them together. In the last part of the function it also checks if any digit is left behind. Then returned the output and wrote it in output file. Also printed the output file and closed the file to make the code
#work properly. Time complexity of merge sort is O(NlogN)