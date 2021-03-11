"""
09. 기본 탐색 알고리즘
난이도: 중상
유형: 이진 탐색
추천 풀이 시간: 1시간

O(M * logC)
"""
from collections import deque
import sys

input = sys.stdin.readline
n, m = list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]
min_value, max_value = 1, 0

for _ in range(m):
    x , y, weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    max_value = max(max_value, weight)

start, end = map(int ,input().split())


def bfs(mid):
    queue = deque([start])
    visited = [0] * (n + 1)
    visited[start] = 1

    while queue:
        x = queue.popleft()        

        for y, weight in adj[x]:

            # 아직 방문하지 않았고 무게 제한에 걸리지 않을 경우
            if not visited[y] and mid <= weight:
                visited[y] = 1
                queue.append(y)

                if y == end: return True

    return False


while min_value <= max_value:
    mid = (min_value + max_value) // 2

    if bfs(mid):
        # 이동 가능
        min_value = mid + 1
    else:
        # 이동 불가
        max_value = mid - 1

print(max_value)