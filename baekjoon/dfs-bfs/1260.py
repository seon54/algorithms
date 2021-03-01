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

def dfs(arr, start):
    visited, stack = deque(), [start]

    while stack:
        node = stack.pop()
        if str(node) not in visited:
            visited.append(str(node))
            arr[node].sort(reverse=True)
            stack.extend(arr[node])

    print(' '.join(visited))


def bfs(arr, start):
    visited, queue = deque(), deque([start])

    while queue:
        node = queue.popleft()
        if str(node) not in visited:
            visited.append(str(node))
            arr[node].sort()
            queue.extend(arr[node])

    print(' '.join(visited))


n, m, v = map(int, input().split())
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())   
    arr[a].append(b)
    arr[b].append(a)

dfs(arr, v)
bfs(arr, v)