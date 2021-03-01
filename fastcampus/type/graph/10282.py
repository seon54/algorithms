"""
16. 그래프 고급 탐색 - 핵심유형
https://www.acmicpc.net/problem/10282

제목: 해킹
난이도: 중
유형: 다익스트라
풀이 시간: 50분
"""
import heapq


def dijkstra(start):
    q = []
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    
    heapq.heappush(q, (distance[start], start))

    while q:
        cur_dis, cur_node = heapq.heappop(q)

        if distance[cur_node] < cur_dis:
            continue

        for i in graph[cur_node]:
            new_dis = cur_dis + i[0]

            if new_dis < distance[i[1]]:
                distance[i[1]] = new_dis                
                heapq.heappush(q, (new_dis, i[1]))

    distance = [i for i in distance if i != float('inf')]
    return len(distance), max(distance)


for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))

    print(*dijkstra(c))

##################################################################

import heqpq
import sys

input = sys.stdin.readline

def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distances[start] = 0

    while heap_data:
        dist, now = heapq.heappop(heap_data)

        if distances[now] < dist:
            continue

        for i in adj[now]:
            cost = dist + i[1]
            if distances[i[0]] > cost:
                distances[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))

for _ in range(int(input())):
    n, m, start = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    distances = [1e9] * (n + 1)

    for _ in range(m):
        x, y, cost = map(int, input().split())
        adj[y].append((x, cost))

    dijkstra(start)
    cnt = 0
    max_distance = 0

    for i in distances:
        if i != 1e9:
            cnt += 1

            if i > max_distance:
                max_distance = i

    print(cnt, max_distance)


