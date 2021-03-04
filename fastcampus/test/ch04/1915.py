"""
동적계획법 - 05.문제풀이

https://www.acmicpc.net/problem/1915
가장 큰 정사각형

"""

N, M = map(int, input().split())
A = [[0] * (M + 1) for _ in range(N + 1)]
result = 0

# DP[i][j] = i, j까지 왔을 때 가장 큰 정사각형 한 변의 길이
DP = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for idx, j in enumerate(list(map(int, input()))):
        A[i][idx + 1] = j

# DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if A[i][j]:
            DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1
            result = DP[i][j] if DP[i][j] > result else result

print(result ** 2)