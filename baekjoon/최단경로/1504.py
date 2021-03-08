import heapq
import sys


input, INF = sys.stdin.readline, 1e9
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)        

        if distance[now] < dist:
            continue

        for cost, node in graph[now]:
            new_cost = dist + cost

            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(q, (new_cost, node))

    return distance

 
start = dijkstra(1)
v1_dst = dijkstra(v1)
v2_dst = dijkstra(v2)
result = min(start[v1] + v1_dst[v2] + v2_dst[n], start[v2] + v2_dst[v1] + v1_dst[n])

print(result if result < INF else -1)