# Kruskal's algorithm


graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (11, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()


def find_parent(node):

    if parent[node] != node:
        return find_parent(parent[node])
    return parent[node]


def union(start, end):
    start_root = find_parent(start)
    end_root = find_parent(end)

    if rank[start_root] > rank[end_root]:
        parent[end_root] = start_root
    else:
        parent[start_root] = end_root
        if rank[start_root] == rank[end_root]:
            rank[end_root] += 1


def kruskal(graph):
    mst = list()

    # 초기화
    for node in graph['vertices']:
        parent[node] = node
        rank[node] = 0

    # 간선 기준 정렬
    edges = graph['edges']
    edges.sort()

    # 간선 연결
    for edge in edges:
        weight, start, end = edge

        if find_parent(start) != find_parent(end):
            union(start, end)
            mst.append(edge)

    return mst