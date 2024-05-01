############################################ Task 4  ###############################################
####################################################################################################

def min_coins(N, X, denominations):
    dp = [float('inf')] * (X + 1)
    dp[0] = 0  # Base case: 0 coins needed to make up amount 0

    for coin in denominations:
        # Update the dp array for each possible amount
        for amount in range(coin, X + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Check if it's possible to make up the target amount
    if dp[X] == float('inf'):
        return -1
    else:
        return dp[X]



#Specify input file path
input_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab7/task4/input.txt'
output_path = 'C:/Users/ASUS/Desktop/cse221_spring_2024/Lab7/task4/output.txt'
#Open file
inp = open(input_path, 'r')
out = open(output_path, 'w')

# Input
N, X = map(int, inp.readline().split())
denominations = list(map(int, inp.readline().split()))

# Output
print(min_coins(N, X, denominations))
out.write(str(min_coins(N, X, denominations)))

out.close()

#Explanation
# Taking input from specified file and getting N(number of different coin dimension) and X(target amount of money). In min_coins() sending N, x and dimensions. Initializing an array to store the minimum number of coins required for each amount.
# Iterating through each coin denomination and updating dp array for each possible amount. Lastly checking if its possible to make target amount and returning output and printing.