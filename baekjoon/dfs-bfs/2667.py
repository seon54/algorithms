###### cnt, check 확인 주의 !!!


from collections import deque


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
result = []


def bfs(a, b):
    cnt = 1
    q = deque([(a, b)])
    check[a][b] = 1

    while q:
        a, b = q.popleft()
        
        for i in range(4):
            x, y = a + dx[i], b + dy[i]

            if 0 <= x < n and 0 <= y < n and graph[x][y] and not check[x][y]:
                cnt += 1
                q.append((x, y))
                check[x][y] = 1
                
    result.append(cnt)


for i in range(n):
    for j in range(n):
        if graph[i][j] and not check[i][j]:
            bfs(i, j)


result.sort()
print(len(result))
for i in result:
    print(i)