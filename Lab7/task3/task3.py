def count_ways_to_climb_stairs(N):
    if N <= 1:
        return 1
    # Create an array to store the number of ways to reach each step
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    # Iterate through the steps and calculate the number of ways to reach each step
    for i in range(2, N + 1):
        # The number of ways to reach the current step is the sum of the ways to reach the previous two steps
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N]

# Input
N = int(input())

# Output
print(count_ways_to_climb_stairs(N))