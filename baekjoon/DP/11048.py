from copy import deepcopy
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
check = deepcopy(arr)

for i in range(1, m):
    check[0][i] += check[0][i - 1]

for i in range(1, n):
    check[i][0] += check[i - 1][0]

for i in range(1, n):
    for j in range(1, m):
        check[i][j] += max(check[i - 1][j], check[i][j - 1], check[i - 1][j - 1])

print(check[n - 1][m - 1])