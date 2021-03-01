"""
15. 그래프 기본 탐색 - 핵심유형
https://www.acmicpc.net/problem/1325

제목: 효율적인 해킹
난이도: 하
유형: BFS, DFS
풀이 시간: 30분
"""
from collections import deque


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
result = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)


def bfs(node):
    q = deque([node])
    check = [0] * (n + 1)
    
    while q:
        x = q.popleft()        
        check[x] = 1
        result[node] += 1

        print(x, result[node])

        for e in graph[x]:
            if not check[e]:
                check[e] = 1
                q.append(e)


for i in range(1, n + 1):
    bfs(i)

for i, v in enumerate(result):
    if v == max(result):
        print(i, end=' ')

########################################################################

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[y].append(x)


def bfs(v):
    q = deque([v])
    visited = [False] * (n + 1)
    visited[v] = True
    count = 1

    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count += 1

    return count

result, max_value = [], -1

for i in range(1, n + 1):
    c = bfs(i)

    if max_value < c:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c

for e in result:
    print(e, end=' ')