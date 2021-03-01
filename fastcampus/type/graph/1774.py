"""
16. 그래프 고급 탐색 - 핵심유형
https://www.acmicpc.net/problem/1774

제목: 우주신과의 교감
난이도: 중
유형: 최소 신장 트리
풀이 시간: 40분

- 2차원 좌표가 주어졌을 때 모든 좌표를 잇는 최소 신장 트리
- 2차원 좌표 상의 점을 잇는 통로 고려해야 함
- 점점의 개수 N이 최대 1,000 이므로 가능한 통로의 개수는 약 N^2
- 크루스칼 알고리즘은 간선의 개수가 E일 때 O(E log E)
"""
import math
import sys


def get_distance(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return math.sqrt(pow(x, 2) + pow(y, 2))


def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(a, b):
    a = find(a)
    b = find(b)
    return a == b


edges, parent, locations = [], {}, []
n, m = map(int, sys.stdin.readline().split())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    locations.append((a, b))

length = len(locations)

for i in range(length - 1):
    for j in range(i + 1, length):
        edges.append((i + 1, j + 1, get_distance(locations[i], locations[j])))

for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    a, b = map(int, input().split())
    union(a, b)

edges.sort(key=lambda x:x[2])

result = 0

for a, b, cost in edges:
    if not find_parent(a, b):
        union(a, b)
        result += cost

print(f'{result:.2f}')