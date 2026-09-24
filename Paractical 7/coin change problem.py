def coin_change(coins, amount):
    # Create DP array
    dp = [float('inf')] * (amount + 1)
    # 0 coins are needed to make amount 0
    dp[0] = 0
    # Calculate minimum coins for every amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount]
# User input
n = int(input("Enter number of coins: "))
coins = list(map(int, input("Enter coin values: ").split()))
amount = int(input("Enter amount: "))
result = coin_change(coins, amount)
if result == float('inf'):
    print("Amount cannot be formed")
else:
    print("Minimum number of coins:", result)