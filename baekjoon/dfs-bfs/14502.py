"""
0: 빈 칸, 1: 벽, 2: 바이러스

- 벽 3개를 세우는 모둔 경우의 수 계산
- 안전 영역 크기는 dfs/bfs 이용해 계산

    1. 벽 세우고 안전 영역 확인
    2. 초기화, DFS 돌리고 안전영역 확인
    3. DFS 통해 바이러스 퍼트리기
"""

#### dfs
import sys


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
result = 0


# 바이러스 퍼트리기
def dfs(a, b):
    for i in range(4):
        x, y = a + dx[i], b + dy[i]

        if 0 <= x < n and 0 <= y < m and not temp[x][y]:
            temp[x][y] = 2
            dfs(x, y)


# 벽 세우기
def wall(x):
    global result
    cnt = 0

    if x == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    dfs(i, j)

        for i in temp:
            cnt += i.count(0)        

        result = max(cnt, result)
        return

    for i in range(n):
        for j in range(m):
            if not graph[i][j]:
                graph[i][j] = 1
                wall(x + 1)
                graph[i][j] = 0

wall(0)
print(result)

#### bfs

from collections import deque
import copy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
result = 0


def bfs():
    global result
    q = deque()
    wall = copy.deepcopy(graph)

    # 바이러스 찾기
    for i in range(n):
        for j in range(m):
            if wall[i][j] == 2:
                q.append([i, j])

    # 바이러스 퍼트리기
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not wall[nx][ny]:
                wall[nx][ny] = 2
                q.append([nx, ny])

    cnt = 0

    for i in wall:
        cnt += i.count(0)

    result = max(result, cnt)


def wall(x):
    if x == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if not graph[i][j]:
                graph[i][j] = 1
                wall(x + 1)
                graph[i][j] = 0


wall(0)
print(result)

