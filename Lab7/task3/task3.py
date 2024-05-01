############################################ Task 3  ###############################################
####################################################################################################

def count_ways_to_climb_stairs(N):
    if N <= 1:
        return 1
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N + 1):
        # The number of ways to reach the current step is the sum of the ways to reach the previous two steps
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N]



#Specify input file path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab7/task3/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab7/task3/output.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')

# Input
N = int(inp.readline())

# Output
print(count_ways_to_climb_stairs(N))
out.write(str(count_ways_to_climb_stairs(N)))

out.close()

#Explanation
# Here, the frog, can climb a staircase with N steps, starting from the 0th step. so, initializing an array dp to store the number of ways to reach each step, then iterates through steps, updating dp with the sum of ways to reach the previous two steps.
# Finally, it returns the count of ways to reach the Nth step.