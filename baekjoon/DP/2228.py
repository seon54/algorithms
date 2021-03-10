# dp[n][m] = dp[k-2][m-1] + sum(k, n)

n, m = map(int, input().split())
arr = [0] * (n + 1)
dp = [[-1] * (n // 2 + 1) for _ in range(n + 1)]
dp[0][0] = 0
min_ = -32768 * 101


def solve(n, m):
    if not m: return 0
    if n <= 0: return min_
    if dp[n][m] != -1: return dp[n][m]

    dp[n][m] = solve(n - 1, m)
    sum_ = 0

    for i in range(n, 0, -1):

        # 누적합 이용해서 1개의 구간 구하기 (i부터 n까지의 구간)
        sum_ += arr[i]

        # 인접하지 않는 범위에서 m - 1개 구간의 최대합 구하기
        temp = solve(i - 2, m - 1) + sum_
        dp[n][m] = max(temp, dp[n][m])
    
    return dp[n][m]


for i in range(1, n + 1):
    arr[i] = int(input())

print(solve(n, m))
