"""
16. 그래프 고급 탐색 - 핵심유형
https://www.acmicpc.net/problem/5719

제목: 거의 최단 경로
난이도: 중
유형: 다익스트라
풀이 시간: 50분

- 최단 경로에 포함되는 모든 간선을 추적
- 추적한 경로 제외 후, 재탐색
- BFS 로 추적
"""
from collections import deque
import heapq
import sys


def dijkstra():
    q, distance[start] = [], 0
    heapq.heappush(q, (0, start))

    while q:
        cur_dis, cur_node = heapq.heappop(q)

        if distance[cur_node] < cur_dis:
            continue        
        else:
            for node, dis in graph[cur_node]:
                new_dis = cur_dis + dis

                if new_dis < distance[node] and not dropped[cur_node][node]:
                    distance[node] = new_dis
                    heapq.heappush(q, (new_dis, node))
                

def bfs():
    q = deque()
    q.append(d)

    while q:
        now = q.popleft()
        if now == s:
            continue
        for prev, cost in reversed_graph[now]:
            if distance[now] == distance[prev] + cost:
                dropped[prev][now] = True
                q.append(prev)


while True:
    n, m = map(int, sys.stdin.readline().split())

    if n == 0 :
        break

    graph = [[] for _ in range(n + 1)]
    reversed_graph = [[] for _ in range(n + 1)]
    s, d = map(int, sys.stdin.readline().split())

    for _ in range(m):
        u, v, p = map(int, sys.stdin.readline().split())
        graph[u].append((v, p))   # (정점, 거리)
        reversed_graph[v].append((u, p))

    dropped = [[False] * (n + 1) for _ in range(n + 1)]
    distance = [1e9] * (n + 1)
    dijkstra()
    bfs()
    distance = [1e9] * (n + 1)
    dijkstra()

    if distance[d] != 1e9:
        print(distance[d])
    else:
        print(-1)