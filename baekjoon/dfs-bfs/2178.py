from collections import deque


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
check = [[0] * m for _ in range(n)]
path = [[0] * m for _ in range(n)]
path[0][0] = 1


def bfs(a, b):
    q = deque([(a, b)])
    check[a][b] = 1

    while q:
        a, b = q.popleft()

        for i in range(4):
            x, y = a + dx[i], b + dy[i]

            if 0 <= x < n and 0 <= y < m and graph[x][y] and not check[x][y]:
                path[x][y] = path[a][b] + 1
                check[x][y] = 1
                q.append((x ,y))


for i in range(n):
    for j in range(m):
        if graph[i][j] and not check[i][j]:
            bfs(i, j)

print(path[n - 1][m - 1])