from collections import deque
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    team = list(map(int, input().split()))
    m = int(input())    

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for idx, t in enumerate(team):
        indegree[t] = idx
        graph[t] += team[idx + 1:]

    for _ in range(m):
        a, b = map(int, input().split())
        a_idx, b_idx = team.index(a), team.index(b)

        # 인덱스 값이 크면 진입차수가 커짐

        if a_idx < b_idx:
            # 올해는 a의 인덱스 값이 더 큼
            indegree[a] += 1
            indegree[b] -= 1
            graph[a].remove(b)
            graph[b].append(a)
        else:
            indegree[b] += 1
            indegree[a] -= 1
            graph[b].remove(a)
            graph[a].append(b)

    result = []
    q = deque()

    for i in range(1, n + 1):
        if not indegree[i]:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if not indegree[i]:
                q.append(i)

    if len(result) == n:
        print(*result)
    else:
        print('IMPOSSIBLE')


