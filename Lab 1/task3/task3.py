##################### Task 3  #####################
####################################################

# Selection Sort            #For minimum swaping we used selection sort
def selection_sort(array):
  for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
      if array[min_idx] > array[j]:
        min_idx = j
    array[i], array[min_idx] = (array[min_idx], array[i])
  return array


#Reading input file
inp3 = open('input3.txt', 'r')
#Generating output file
out3 = open('output3.txt', 'w')

#Reading first line which is size
size = int(inp3.readline())
idd = list(map(int, inp3.readline().split(" ")))   # Convert ['1','2'] to [1,2]
numbers = list(map(int, inp3.readline().split(" ")))   # Convert ['1','2'] to [1,2]


# Creating a dictionary [numbers:ID]
pair = {}  
for i in range(size):
  if numbers[i] in pair.keys():
    pair[numbers[i]].append(idd[i])
  else:
    pair[numbers[i]] = [idd[i]]

sortedsorted_numbers = selection_sort(numbers)
descending_sorted_numbers = sortedsorted_numbers[::-1]   # Sorting Numbers

for idd in pair:
  selection_sort(pair[idd])        # Sorting ID

idx_c = 0
i = 0

while (i<size):
  for num,idd in pair.items():
    if descending_sorted_numbers[i] == num:           # ID-Number Maping
      for j in range(len(idd)):
        out3.write(f"ID: {idd[j]} Mark: {num}\n")        # Write Output
        idx_c += 1
  i = idx_c              # Index of next number to print

#Closing file for safety
out3.close()

###Explanation
# Here I am using selection sort to use minimum number of swaping. I am creating number:id dictionary as the number wise I have to sort.
# Then sorted in descending order. After that I have sorted value of every key. Then I simply just printed output file in the designated file.