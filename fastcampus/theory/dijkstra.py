# 우선순위 큐 사용

import heapq


def dijkstra(graph, start):
    """
    heapq.heappush(heap, item)
        heap -> []
        item -> (1, value)
    heapq.heappop(heap)
    """
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for node, weight in distances[current_node].items():
            distance = current_distance + weight

            if distance < distances[node]:
                distances[node] = distance
                heapq.heappush(queue, (distance, node))


graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(graph, 'A'))