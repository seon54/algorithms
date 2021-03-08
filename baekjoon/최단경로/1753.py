import heapq

INF = 1e9
v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v)) # 거리, 노드 순


def dijkstra(start):
    q = []    
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for cost, node in graph[now]:            
            new_cost = cost + dist

            if new_cost < distance[node]:
                distance[node] = new_cost
                q.append((new_cost, node))

dijkstra(k)

for i in distance[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)