from collections import deque


"""
bfs 로 풀어야 하는 문제, dfs 로 풀 경우 값이 틀림

[test]
5 6
101010
111111
000001
111111
111111
"""

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
check = [[0 for _ in range(m)] for _ in range(n)]
check2 = [[0 for _ in range(m)] for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
cnt = 0


def dfs(a, b):
    global cnt

    if check[a][b]:
        return

    cnt += 1
    check[a][b] = cnt

    for i in range(4):
        x, y = a + dx[i], b + dy[i]

        if x < 0 or y < 0 or x >= n or y >= m or check[x][y] or arr[x][y] == '0':
            continue

        dfs(x, y)


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    check2[a][b] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or check2[nx][ny] or arr[nx][ny] == '0':                
                continue
    
            check2[nx][ny] = check2[x][y] + 1

            if nx == n - 1 and ny == m - 1:
                print(check2[nx][ny])
                break

            queue.append((nx, ny))


# dfs(0, 0)
# print(check)

bfs(0, 0)
print(check2)
