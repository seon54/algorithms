from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
result = 0


def bfs():
    q = deque([(0, 0)])
    check = [[0] * m for _ in range(n)]
    check[0][0] = 1

    while q:
        a, b = q.popleft()

        for i in range(4):
            x, y = a + dx[i], b + dy[i]

            if 0 <= x < n and 0 <= y < m and not check[x][y]:

                if 1 <= arr[x][y]:
                    arr[x][y] += 1
                else:
                    q.append((x, y))
                    check[x][y] = True


def melt():
    melted = False

    for i in range(n):
        for j in range(m):

            if 3 <= arr[i][j]:
                arr[i][j] = 0
                melted = True
            elif arr[i][j] == 2:
                arr[i][j] = 1

    return melted

while True:
    bfs()

    if melt():
        result += 1
    else:
        print(result)
        break