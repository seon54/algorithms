from collections import defaultdict
from heapq import *


def prim(edges: list, start_node:str):
    mst = []    # 결과
    adjacent_edges = defaultdict(list)  # 모든 간선 정보

    # edges 에서 모든 간선 정보 가져오기
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_node = set(start_node)    # 연결된 노드
    candidate_edges = adjacent_edges[start_node]    # 연결할 노드 목록
    heapify(candidate_edges)

    while candidate_edges:
        weight, n1, n2 = heappop(candidate_edges)

        # 연결된 노드인지 확인
        if n2 not in connected_node:
            connected_node.add(n2)
            mst.append((weight, n1, n2))

            # 연결된 노드에 추가 후, 인접 노드를 연결할 노드 목록에 추가하기
            for weight, n1, n2 in adjacent_edges[n2]:
                if n2 not in candidate_edges:
                    heappush(candidate_edges, (weight, n1, n2))

    return mst


edges = [
    (7, 'A', 'B'),
    (5, 'A', 'D'),
    (8, 'B', 'C'),
    (9, 'B', 'D'),
    (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'),
    (6, 'D', 'F'),
    (8, 'E', 'F'),
    (9, 'E', 'G'),
    (11, 'F', 'G'),
]


print(prim(edges, 'A'))


def prim2(edges, start_node):
    mst = []
    adjacent_edges = defaultdict(list)

    for edge in edges:
        weight, n1, n2 = edge
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_node = list(start_node)
    candidate_edges = adjacent_edges[start_node]
    heapify(candidate_edges)

    while candidate_edges:
        weight, n1, n2 = heappop(candidate_edges)

        if n2 not in connected_node:
            connected_node.append(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2]:
                weight, n1, n2 = edge
                if n2 not in candidate_edges:
                    heappush(candidate_edges, (weight, n1, n2))
    
    return mst


print(prim2(edges, 'C'))