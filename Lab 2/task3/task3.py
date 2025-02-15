###############################  Task 3 ##################################
##########################################################################

#path declaration
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task3/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task3/output.txt'


# read the file
inp = open(input_path, 'r')
# generate a output file by running the code
out = open(output_path, 'w')


size = int(inp.readline())  #Reading array size
intervals = []


for i in range(size):
    start, end = map(int, inp.readline().strip().split())  #Reading intervals from the file
    intervals.append((start, end))              #Add start and end time tupple in the list created before
    
    
# Sorting the intervals based on end times
intervals.sort(key=lambda x: x[1])


completed_tasks = []
current_end_time = -1         #Currrent time is -1 because the task is sorted and first tupple will always be counted

for i in range(len(intervals)):
  if intervals[i][0] >= current_end_time:                    #if start time greater than or equal end time
    completed_tasks.append(intervals[i])
    current_end_time = intervals[i][1]                      #current_end_time updated for next comparison
    

# Output
out.write(str(len(completed_tasks)) + "\n")     #Writing on file
print(len(completed_tasks))                     # Length of tuple is the completed task
for task in completed_tasks:
  out.write(f"{task[0]} {task[1]} \n")
  print(task[0], task[1])                     #print

out.close()  #Closing output file for  saving properly


#Explanation
#Here in this problem, I took input from a designated input file, read first line for size and number of people. Then used a loop to get time intervals and then did append those to a list as a tuple.
#I have used tuple as it's constant and faster. Then I have sorted them using sort function respect to end time in ascending order. Then I have chcecked if next tasks start is equal or greater than the current 
#end time. if greater or equal then the person can do that work, else not. If can do the task importing the tuple to completed task list. Here the length is the most task that can be completed and 
#then print all those.