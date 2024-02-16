###############################  Task 4 ################################
##########################################################################

#path declaration
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task4/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab 2/task4/output.txt'


# read the file
inp = open(input_path, 'r')
# generate a output file by running the code
out = open(output_path, 'w')



# Reading task and people
N, M = map(int, inp.readline().split())
intervals = [tuple(map(int, inp.readline().strip().split())) for i in range(N)]  #Reading all intervals and converting to tuple



#Function to minimize code
def max_task(n, m, intervals):
    # Initialize schedule for each person
    schedule = [0] * M

    # Count of tasks completed
    completed_tasks = 0

    # Assign tasks greedily
    for activity in intervals:
        start, end = activity
        
        # Find the earliest available person
        for i in range(M):
            if schedule[i] <= start:
                schedule[i] = end
                completed_tasks += 1
                break
    return completed_tasks


# Sort intervals based on their end times
sorted_on_endtime = sorted(intervals, key=lambda x: x[1])

# Sort intervals based on their start times
sorted_on_starttime = sorted(intervals, key=lambda x: x[0])

#choosing biggest combination of tasks
if(max_task(N, M, sorted_on_endtime) >= max_task(N, M, sorted_on_starttime)):
    out.write(str(max_task(N, M, sorted_on_endtime)))
    print(max_task(N, M, sorted_on_endtime))
else:
    out.write(str(max_task(N, M, sorted_on_starttime)))
    print(max_task(N, M, sorted_on_starttime))

out.close()         #Closing output file to save and work properly 
