"""
15. 그래프 기본 탐색 - 핵심유형
https://www.acmicpc.net/problem/2606

제목: 바이러스
난이도: 하
유형: BFS, DFS
풀이 시간: 30분
"""
from collections import deque

c, n = int(input()), int(input())
arr = [[] for _ in range(c + 1)]
check = [False] * (c + 1)
check[1] = True

for _ in range(n):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def bfs():
    q = deque([1])    
    cnt = 0

    while q:
        node = q.popleft()        
        cnt += 1

        for e in arr[node]:
            if not check[e]:
                check[e] = True
                q.append(e)

    return cnt - 1

print(bfs())

############################################################

# 컴퓨터 수가 적으므로 DFS로 푸는 것이 유리함 (BFS보다 빠름)
# 컴퓨터 수 (100) 은 파이썬의 재귀 횟수 초과하지 않음

n, m = int(input()), int(input())
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)


def dfs(node):
    global count
    count += 1
    visited[node] = True

    for e in adj[node]:
        if not visited[e]:
            dfs(e)

dfs(1)
print(count - 1)