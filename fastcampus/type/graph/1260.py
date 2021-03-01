"""
14. 그래프 기본 탐색 - 기초 문제
https://www.acmicpc.net/problem/1260   

제목: DFS 와 BFS
난이도: 하
유형: DFS, BFS
풀이 시간: 30분
"""

from collections import deque


def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)


n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
