def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount]
n = int(input("Enter number of coins: "))
coins = list(map(int, input("Enter coin values: ").split()))
amount = int(input("Enter amount: "))
result = coin_change(coins, amount)
if result == float('inf'):
    print("Amount cannot be formed")
else:
    print("Minimum number of coins:", result)