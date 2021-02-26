# 내 풀이
t = int(input())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def find(a, b, n, m):
    if (a, b) in cbg:
        return

    cbg.append((a, b))

    for i in range(4):
        x, y = a + dx[i], b + dy[i]

        if x < 0 or x >= n or y < 0 or y >= m or array[x][y] == 0 or (x, y) in cbg:
            continue
                
        find(x, y, n, m)


for _ in range(t):
    cbg, cnt = [], 0
    m, n, k = map(int, input().split())
    array = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        i, j = map(int, input().split())
        array[j][i] = 1

    for i in range(n):
        for j in range(m):

            if array[i][j] == 1 and (i, j) not in cbg:
                cnt += 1
                find(i, j, n, m)

    print(cnt)

# dfs
import sys
sys.setrecursionlimit(10000)


T = int(input())
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):  
    if check[x][y]:
        return

    check[x][y] = 1

    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]

        if B[xx][yy] == 0 or check[xx][yy]:
            continue
        dfs(xx, yy)
    

for _ in range(T):   
    M, N, K = map(int, input().split())
    B = [[0 for _ in range(M + 2)] for _ in range(N + 2)]   # 위아래좌우 0으로 한 줄씩 더 채워줌
    check = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
    ans = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y + 1][X + 1] = 1

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if B[i][j] == 0 or check[i][j]:
                continue
            dfs(i, j)
            ans += 1

    print(ans)