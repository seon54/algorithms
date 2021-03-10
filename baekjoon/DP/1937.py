import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
dp = [[0] * n for _ in range(n)]
result = 0


# 반환값: arr[a][b] 에서 시작할 때의 최대값
def dfs(a, b):
    if dp[a][b]: return dp[a][b]
    dp[a][b] = 1

    for i in range(4):
        x, y = a + dx[i], b + dy[i]

        if 0 <= x < n and 0 <= y < n and arr[a][b] < arr[x][y]:
            dp[a][b] = max(dp[a][b], dfs(x, y) + 1)

    return dp[a][b]



for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)