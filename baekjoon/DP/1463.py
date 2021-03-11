import sys

# 점화식 dp[n] = min(dp[n // 3] + 1, dp[n // 2] + 1, dp[n - 1] + 1)

n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if not i % 2:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if not i % 3:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])
