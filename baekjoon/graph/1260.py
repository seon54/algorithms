from collections import deque


def dfs(graph, start):
    visited, stack = deque(), [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if graph.get(node, None):
                stack.extend(graph[node])

    print(' '.join(list(map(str, visited))))


def bfs(graph, start):
    visited, queue = deque(), deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if graph.get(node, None):
                queue.extend(graph[node])

    print(' '.join(list(map(str, visited))))


d = dict()
n, m, v = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())

    if a in d:
        d[a].append(b)
    else:
        d[a] = [b]

    if b in d:
        d[b].append(a)
    else:
        d[b] = [a]

for l in d.values():
    l.sort(reverse=True)

dfs(d, v)

for l in d.values():
    l.sort()

bfs(d, v)

########################################################################

n, m, v = map(int, input().split())

adj = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

def dfs(v, hist, adj):
    hist.append(v)
    for i in range(1, n + 1):
        if adj[v][i] and i not in hist:
            hist = dfs(i, hist, adj)
    return hist

def bfs(v, adj):
    q = [v]
    hist = [v]
    while q:
        now = q.pop(0)
        for i in range(1, n + 1):
            if adj[now][i] and i not in hist:
                q.append(i)
                hist.append(i)
    return hist

print(' '.join(map(str, dfs(v, [], adj))))
print(' '.join(map(str, bfs(v, adj))))
