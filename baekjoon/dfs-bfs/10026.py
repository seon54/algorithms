import sys

sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
arr = [list(input()) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
check1 = [[0] * n for _ in range(n)]
check2 = [[0] * n for _ in range(n)]
rg = ['R', 'G']
ans1, ans2 = 0, 0


def dfs(a, b):
    check1[a][b] = 1

    for i in range(4):
        x, y = a + dx[i], b + dy[i]

        if 0 <= x < n and 0 <= y < n and arr[x][y] == arr[a][b] and not check1[x][y]:
            dfs(x, y)


def dfs_rg(a, b):
    check2[a][b] = 1


    for i in range(4):
        x, y = a + dx[i], b + dy[i]

        if 0 <= x < n and 0 <= y < n and not check2[x][y]:
            if arr[a][b] in rg and arr[x][y] in rg:
                dfs_rg(x, y)
            elif arr[x][y] == arr[a][b]:
                dfs_rg(x, y)            
             

for i in range(n):
    for j in range(n):
        if not check1[i][j]:
            dfs(i, j)
            ans1 += 1

        if not check2[i][j]:
            dfs_rg(i, j)
            ans2 += 1

print(ans1, ans2)