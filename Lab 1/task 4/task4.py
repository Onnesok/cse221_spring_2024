##################### Task 4  #####################
####################################################

# Insertion Sort        [We use this sort for Laarge/Multiple Data]
def insertionSort(schedule):
  for i in range(1, len(schedule)):
    train, dest, time = schedule[i]
    hour = int(time.split(":")[0])
    j = i - 1
    prevTrain, prevDest, prevTime = schedule[j][0], schedule[j][1], schedule[j][2]
    prevHour = int(prevTime.split(":")[0])
    while j>=0 and (prevTrain > train or (prevTrain == train and prevHour < hour)):
      schedule[j+1] = schedule[j]
      j -= 1
      prevTrain, prevDest, prevTime = schedule[j][0], schedule[j][1], schedule[j][2]
      prevHour = int(prevTime.split(":")[0])
    schedule[j+1] = (train, dest, time)
  return schedule

# Read the file
inp4 = open("input4.txt","r")
# Generate a output file by running the code
out4 = open("output4.txt","w")

total = int(inp4.readline())

schedule = []

for i in range(total):
  info = inp4.readline().split(" ")
  name = info[0]
  district = info[-3]
  time = info[-1][:-1]
  schedule.append([name,district,time])

sortedSchedule = insertionSort(schedule)

for i in range(total):
  out4.write(f"{sortedSchedule[i][0]} will departure for {sortedSchedule[i][1]} at {sortedSchedule[i][2]}\n")

# must close the file; Otherwise the output will not Update/generated
out4.close()


###Explanation
# Here I have used insertion sort to handle large number of data.The insertionSort function iterates through the schedule and compares each train's departure time and name with the previous ones.
#It rearranges the elements in a way that ensures the schedule is sorted based on departure time and, in case of a tie, by train name.
# The main loop extracts info by spliting and sends them to schedule list. Then schedule is sorted using insertion sort and output
# is written in designated file.