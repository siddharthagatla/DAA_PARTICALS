def matrix_chain(p):
    n = len(p) - 1
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    # length = number of matrices in the chain
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')
            # Try every possible split
            for k in range(i, j):
                dp[i][j] = min(dp[i][j],dp[i][k] +dp[k + 1][j] + p[i - 1] * p[k] * p[j] )
    return dp[1][n]
# User input
n = int(input("Enter number of matrices: "))
p = []
print("Enter dimensions:")
for i in range(n + 1):
    value = int(input(f"p[{i}] = "))
    p.append(value)
result = matrix_chain(p)
print("Minimum number of scalar multiplications:", result)