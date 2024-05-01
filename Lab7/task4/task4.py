def min_coins_needed(N, X, denominations):
    # Initialize an array to store the minimum number of coins required for each amount
    dp = [float('inf')] * (X + 1)
    dp[0] = 0  # Base case: 0 coins needed to make up amount 0

    # Iterate through each coin denomination
    for coin in denominations:
        # Update the dp array for each possible amount
        for amount in range(coin, X + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Check if it's possible to make up the target amount
    if dp[X] == float('inf'):
        return -1
    else:
        return dp[X]

# Input
N, X = map(int, input().split())
denominations = list(map(int, input().split()))

# Output
print(min_coins_needed(N, X, denominations))