"""
33. 동적계획법 - 02.문제풀이 A

https://www.acmicpc.net/problem/1932
정수삼각형
필수 유형
난이도: 하
"""

n = int(input())
a = [[0] * (n + 1) for _ in range(n + 1)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

# a[i][j] : i, j에 도착했을 때 최대값 저장
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))

    for j in range(1, i + 1):
        a[i][j] = tmp[j - 1]

# DP 
for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + a[i][j]