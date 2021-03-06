from collections import deque
from copy import deepcopy

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
check = deepcopy(arr)
cnt, result = 1, 1e9


# 섬을 찾아서 각자 번호 부여하기
def numbering(a, b, cnt):
    q = deque([(a, b)])

    while q:
        a, b = q.popleft()

        for i in range(4):
            x, y = a + dx[i], b + dy[i]

            if 0 <= x < n and 0 <= y < n:
                if check[x][y] == 1:
                    check[x][y] = cnt
                    q.append((x, y))


for i in range(n):
    for j in range(n):
        if check[i][j] == 1:
            cnt += 1
            check[i][j] = cnt
            numbering(i, j, cnt)


def bfs(island_num):
    global result
    dist = [[-1] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if check[i][j] == island_num:
                q.append((i, j))
                dist[i][j] = 0


    while q:
        a, b = q.popleft()

        for i in range(4):
            x, y = a + dx[i], b + dy[i]

            if 0 <= x < n and 0 <= y < n:

                # 다른 섬에 도착했을 경우
                if check[x][y] and check[x][y] != island_num:
                    result = min(result, dist[a][b])
                    return

                # 바다에 있는 경우 
                if not check[x][y] and dist[x][y] == -1:
                    dist[x][y] = dist[a][b] + 1
                    q.append((x, y))


for i in range(2, cnt + 1):
    bfs(i)

print(result)