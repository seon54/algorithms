from collections import deque


INF = 1e9

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
shark_size = 2
now_x, now_y = 0, 0
result, ate = 0, 0

# 상어 위치 확인
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9: 
            now_x, now_y = i, j
            graph[i][j] = 0
            break

# 모든 위치까지의 최단 거리만 계산
def bfs():
    dist = [[0] * n for _ in range(n)] #  거리 초기화  (0은 갈 수 없는 곳)
    q = deque([(now_x, now_y)])

    while q:
        a, b = q.popleft()

        for i in range(4):
            x, y = a + dx[i], b + dy[i]

            if 0 <= x < n and 0 <= y < n and not dist[x][y] and graph[x][y] <= shark_size:
                dist[x][y] = dist[a][b] + 1
                q.append((x, y))

    return dist

# 최단 거리 테이블이 주어졌을 때, 먹을 물고기 찾기
def find(dist):
    x, y, min_dist = 0, 0, INF

    for i in range(n):
        for j in range(n):
            if dist[i][j] and 1 <= graph[i][j] < shark_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]

    if min_dist == INF:
        return None
    else:
        return x, y, min_dist


while True:
    # 먹을 수 있는 물고기 위치 찾기
    value = find(bfs())
    if value:
        now_x, now_y = value[0], value[1]
        result += value[2]

        # 먹은 물고기 처리
        graph[now_x][now_y] = 0
        ate += 1
        if shark_size <= ate:
            shark_size += 1
            ate = 0
    else:
        print(result)
        break

