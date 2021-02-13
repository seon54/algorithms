# 정점(Vertex) 또는 노드와 간선(Edge)로 표현

# BFS
# 노드 수: V, 간선 수: E 시간 복잡도 O(V + E)

def bfs(graph:dict , start_node):
    visited = list()
    unvisited = list()

    unvisited.append(start_node)

    while unvisited:
        node = unvisited.pop(0)
        if node not in visited:
            visited.append(node)
            unvisited.extend(graph[node])

    return visited
        

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'G', 'H', 'I'],
    'D': ['B', 'E', 'F'],
    'E': ['D'],
    'F': ['D'],
    'G': ['C'],
    'H': ['C'],
    'I': ['C', 'J'],
    'J': ['I']
}

print(bfs(graph, 'A'))

# DFS
# 노드 수: V, 간선 수: E 시간 복잡도 O(V + E)

def dfs(graph, start_node):
    visit_queue = list()
    unvisited_stack = list()

    unvisited_stack.append(start_node)

    while (unvisited_stack):
        node = unvisited_stack.pop()
        if node not in visit_queue:
            visit_queue.append(node)
            unvisited_stack.extend(graph[node])

    return visit_queue

print(dfs(graph, 'A'))