from collections import deque


n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

# arr[x][y] : x를 만들 때 필요한 y의 개수
arr = [[0] * (n + 1) for _ in range(n + 1)] 

for _ in range(int(input())):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))     # y가 있어야 x 를 만들 수 있음
    indegree[x] += 1
    

def topology():
    q = deque()

    for i in range(1, n + 1):
        if not indegree[i]:
            q.append(i)
            arr[i][i] = 1

    while q:
        now = q.popleft()

        for nxt, cnt in graph[now]:
            indegree[nxt] -= 1

            for i in range(1, n + 1):
                arr[nxt][i] += cnt * arr[now][i]
            
            if not indegree[nxt]:
                q.append(nxt)

topology()

for i in range(1, n + 1):
    if arr[n][i]:
        print(i, arr[n][i])