############################# Task 6 #################################
######################################################################
from collections import deque

#Specify path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task6/input1_1.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab4/task6/output1_1.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')
#Read and split
R, H = inp.readline().strip('\n').split(' ')
grid = []

def DFS(grid, visited, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j] or grid[i][j] == '#':       #for invalid cases
        return 0

    visited[i][j] = True
    diamonds = 0

    if grid[i][j] == 'D':       #If d found adding to diamonds
        diamonds += 1
    diamonds += max(DFS(grid, visited, i+1, j), DFS(grid, visited, i-1, j), DFS(grid, visited, i, j+1), DFS(grid, visited, i, j-1))
    visited[i][j] = False

    return diamonds

#Reading inputs and maping in grid
for i in range(int(R)):
    line = inp.readline().strip('\n')
    grid.append(line)

#Visited array for keeping track
visited = [[False]*int(H) for i in range(int(R))]
maxDiamond = 0 #initializing with 0

for i in range(int(R)):
    for j in range(int(H)):
        if grid[i][j] == '.':  # If . then I can go and so checking
            diamonds = DFS(grid, visited, i, j)
            maxDiamond = max(maxDiamond, diamonds)
            
            
print(maxDiamond)            
out.write(str(maxDiamond))


out.close()  #closing output file for safety and saving without delay


#Explanation
# Here I am taking input from file and spliting and then by iteration making a grid for easier traversal. Now Calling dfs function where I am checking first if case is valid or not. Then checking for diamonds and adding if found. Do this recursively and from the return value
# printing the output.
