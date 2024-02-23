################################## Task 3  ##########################################
#####################################################################################
#Define file location
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task3/input3.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab3/task3/output3.txt'

# read the file
f = open(input_path,"r")
# generate a output file by running the code
f2 = open(output_path,"w")

#Aliens
N = int(f.readline())  #Reading first line
array1 = f.readline().split(" ")  #Reading second line and spliting
array1 = list(map(int, array1)) #Maping into an array

def countPair(arr):                # Merge Sort
  if len(arr) > 1:
    mid = len(arr) // 2
    left, count_left = countPair(arr[:mid])
    right, count_right = countPair(arr[mid:])
    sorted_arr, count = CheckAndMerge(left, right)
    total_count = count_left + count_right + count
    return sorted_arr, total_count
  else:
    return arr, 0

def CheckAndMerge(left, right):           # Merge
  merged = []
  count = 0
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] > right[j]:
      merged.append(left[i])
      count += len(right) - j
      i += 1
    else:
      merged.append(right[j])
      j += 1

  merged.extend(left[i:])
  merged.extend(right[j:])
  return merged, count

array, count = countPair(array1)

print(str(count))
f2.write(str(count))  #writing output to file
f2.close()  #Closing output file to work properly

#Explanation
#In this code first defined file path, read 1st and 2nd line and converted second line to an array. Then called the function countpair() where checked if the size is greater than 1 and if yes then used greedy approach. Divided array into half and called again or recursion. Also
#here I've used another variable called count or can say used 2 variables. here first one used for data and count is used for counting. In the last called checkAndMerge() function where I am checking if next element is bigger or smaller than current and if smaller then increasing count
#as it would be a pair. Also extending to check if any element is left behind. Here, I have used modified merged sort and so time complexity becomes O(NlogN) and which is better than n^2.