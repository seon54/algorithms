from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    time[i] = lst[0]

    for pre in lst[1:-1]:
        indegree[i] += 1
        graph[pre].append(i)    # pre에서 i에 갈 수 있음 (pre를 한 후에 i 가능)


def topology():
    result, q = deepcopy(time), deque()

    for i in range(1, n + 1):
        if not indegree[i]:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:            
            indegree[i] -= 1
            result[i] = max(result[i], time[i] + result[now])

            if not indegree[i]:                                
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])


topology()

