n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
check = [[False for _ in range(m)] for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
cnt = 0

def dfs(a, b):
    if check[a][b]:
        return

    check[a][b] = True

    for i in range(4):
        x, y = a + dx[i], b + dy[i]

        if x < 0 or y < 0 or x >= n or y >= m or check[x][y] or arr[x][y] == '1':
            continue

        dfs(x, y)  


for i in range(n):
    for j in range(m):
        if arr[i][j] == '1' or check[i][j]:
            continue
        else:
            dfs(i, j)
            cnt += 1

print(cnt)

# 책 풀이

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        # 상하좌우
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True
    return False


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
