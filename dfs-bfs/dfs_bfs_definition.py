from collections import deque


def depth_first_search(graph: list, v: int, visited: list):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            depth_first_search(graph, i, visited)


def breadth_first_search(graph: list, start: int, visited: list):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph1 = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited1 = [False] * 9

graph2 = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited2 = [False] * 9

depth_first_search(graph1, 1, visited1)
print()
breadth_first_search(graph2, 1, visited2)
