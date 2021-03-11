from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
mn, mx = 1, 0

for _ in range(m):
    x, y, w = map(int, input().split())
    adj[x].append((y, w))
    adj[y].append((x, w))
    mx = max(mx, w)

start, end = map(int, input().split())


def bfs(mid):
    q = deque([start])
    v = [0] * (n + 1)
    v[start] = q

    while q:
        now = q.popleft()

        for y, w in adj[now]:

            if not v[y] and mid <= w:
                q.append(y)
                v[y] = 1

                if y == end: return True

    return False


while mn <= mx:
    mid = (mn + mx) // 2

    if bfs(mid):
        mn = mid + 1
    else:
        mx = mid - 1

print(mx)