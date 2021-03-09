n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)

for i in range(1, k + 1):
    temp = []

    for coin in coins:
        if coin <= i and dp[i - coin] != -1:
            temp.append(dp[i - coin])

    if not temp:
        dp[i] = -1
    
    else:
        dp[i] = min(temp) + 1

print(dp[k])

#############################################

MAX = 100001
dp2 = [MAX] * (k + 1)
dp2[0] = 0

for coin in coins:
    for j in range(coin, k + 1):
        dp2[j] = min(dp2[j], dp2[j - coin] + 1)

print(-1 if dp2[k] == MAX else dp2[k])


