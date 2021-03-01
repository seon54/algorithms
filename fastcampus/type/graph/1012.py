"""
15. 그래프 기본 탐색 - 핵심유형
https://www.acmicpc.net/problem/1012

제목: 유기농배추
난이도: 하
유형: BFS, DFS
풀이 시간: 30분

- 연결 요소의 개수 세기 (출제 비중 높음)
- DFS/BFS 수행한 횟수 세기
- DFS로 풀 경우, sys.setrecursionlimit()
"""
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def dfs(a, b):
    if check[a][b]: return

    check[a][b] = True

    for i in range(4):
        x, y = a + dx[i], b + dy[i]

        if x < 0 or x >= n or y < 0 or y >= m or graph[x][y] == 0 or check[x][y]:
            continue

        dfs(x, y)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    check = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not check[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)

################################################################
import sys
sys.setrecursionlimit(1000000)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    visited[x][y] = True    

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny>= m or visited[nx][ny] or not array[nx][ny]:
            continue

        dfs(nx, ny)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    array = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        array[x][y] = 1

    result = 0

    for i in range(n):
        for j in range(m):
            if array[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1

    print(result)

