from copy import deepcopy
import sys

sys.setrecursionlimit(100000)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
result = 0
max_height = 0

def find_area(height):
    temp = deepcopy(arr)

    for i in range(n):
        for j in range(n):
            if arr[i][j] <= height:
                temp[i][j] = 0

    return temp

def dfs(a, b):
    global check
    check[a][b] = 1

    for i in range(4):
        x, y = a + dx[i], b + dy[i]

        if 0 <= x < n and 0 <= y < n and temp[x][y] and not check[x][y]:
            dfs(x, y)

def loop_func(temp):
    global result
    cnt = 0
    for i in range(n):
        for j in range(n):
            if temp[i][j] and not check[i][j]:
                cnt += 1
                dfs(i, j)
                
    result = max(result, cnt)

for i in range(n):
    for j in range(n):
        if arr[i][j] > max_height:
            max_height = arr[i][j]

for i in range(max_height):
    temp = find_area(i)
    check = [[0] * n for _ in range(n)]
    loop_func(temp)

print(result)