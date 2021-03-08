import heapq
import sys


INF = 1e9
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance1 = [INF] * (n + 1)
distance2 = [[INF] * 2 for _ in range(n + 1)]
result = 0

for _ in range(m):
    a, b, d = map(int, input().split())
    d *= 2
    graph[a].append((d, b))
    graph[b].append((d, a))


def dijkstra(start):
    
    q = []
    heapq.heappush(q, (0, start))
    distance1[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        dist *= -1

        if distance1[now] < dist:
            continue

        for cost, node in graph[now]:
            new_cost = dist + cost
            
            if new_cost < distance1[node]:
                distance1[node] = new_cost
                heapq.heappush(q, (-new_cost, node))


def dijkstra2(start):
    q = []
    heapq.heappush(q, (0, start, 1))
    distance2[start][start] = 0

    while q:
        dist, now, sprint = heapq.heappop(q)
        dist *= -1

        if distance2[now][sprint] < dist:
            continue

        for cost, node in graph[now]:

            if sprint:
                next_sprint = 0
                new_cost = dist + cost // 2
            else:
                next_sprint = 1
                new_cost = dist + cost * 2
            
            if new_cost < distance2[node][next_sprint]:              
                distance2[node][next_sprint] = new_cost
                heapq.heappush(q, (-new_cost, node, next_sprint))


dijkstra(1)
dijkstra2(1)
distance2 = list(map(lambda x: min(x), distance2))

for i in range(2, n + 1):
    if distance1[i] == INF: continue
    if distance1[i] < distance2[i]: result += 1

print(result)
