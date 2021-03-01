from collections import defaultdict, deque
import sys


n, m, k, x = map(int, sys.stdin.readline().split())
v = [0 for _ in range(n + 1)]
d = defaultdict(list)
check = [0 for _ in range(n + 1)]
find = False

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    d[a].append(b)


def bfs(x):
    queue = deque([x])
    count = 0

    while queue:
        z = queue.popleft()
        check[z] = 1

        for i in d[z]:
            if check[i]:
                continue
            queue.append(i)
            
            if not v[i]:
                v[i] = v[z] + 1


bfs(x)

for i, v in enumerate(v):
    if v == k:
        print(i)
        find = True

if not find:
    print(-1)


# 풀이

from collections import deque


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

# bfs
q = deque([x])
while q:
    now = q.popleft()

    for node in graph[now]:
        if distance[node] == -1:
            distance[node] = distance[now] + 1
            q.append(node)

check = False

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
