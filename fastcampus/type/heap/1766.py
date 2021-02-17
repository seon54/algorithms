"""
11. 고급 탐색 알고리즘 - 핵심 유형
제목: 문제집
난이도: 중
유형: 힙, 위상정렬
추천 풀이 시간: 40분

위상정렬 O(V + E)  V: 노드 개수 E: 간선 개수
"""
import heapq

n, m = list(map(int, input().split(' ')))
array = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)    # 연결된 노드의 값

heap = []
result = []

for _ in range(m):
    x, y = map(int, input().split())
    array[x].append(y)
    indegree[y] += 1

print("*****")
print(f'array = {array}')
print(f'indegree = {indegree}')

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

print(f'heap = {heap}')

result = []

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)
print("*****")
print(f'heap = {heap}')

for i in result:
    print(i, end=' ')

