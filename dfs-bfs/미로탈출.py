from collections import deque

"""
5 6
101010
111111
000001
111111
111111
"""

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]    # 상하좌우


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

bfs(0, 0)
print(graph)

################################################################################################

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
check = [[0 for _ in range(m)] for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    check[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx == n - 1 and ny == m - 1:
                print(check[x][y] + 1)
                break
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 0 or check[nx][ny]:
                continue

            check[nx][ny] = check[x][y] + 1
            queue.append((nx, ny))


bfs(0, 0)

