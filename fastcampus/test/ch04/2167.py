"""
동적계획법 - 04.문제풀이

https://www.acmicpc.net/problem/2167
2차원 배열의 합

- 누적합
- 교집합 빼기
"""

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# DP[i][j] = (1, 1)부터 (i, j)까지의 부분합
DP = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        # A[i - 1][j - 1] = (i, j) 자리의 원래 값
        DP[i][j] = DP[i - 1][j] + DP[i][j - 1] - DP[i - 1][j - 1] + A[i - 1][j - 1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[i - 1][y] - DP[x][j -1] + DP[i - 1][j - 1])