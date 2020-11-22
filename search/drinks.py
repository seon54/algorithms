"""
N X M 크기의 얼음틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우
서로 연결되어 있는 것으로 간주한다. 이때 얼음틀의 모양이 주어졌을 때 생성되는 아이스크림의 개수를 구하는 프로그램을 작성하시오.

입력 조건
- 첫번째 줄에 얼음틀의 세로길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 100)
- 두번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
- 이때 구멍이 뚫혀있는 부분은 0, 그렇지 않은 부분은 1이다.

출력 조건
- 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.
"""

# 내 풀이

from collections import deque


n, m = map(int, input().split())
case = list()

for i in range(n):
    case.append(list(map(int, input().split())))


visited = [False] * m


def bfs(graph, start, visited):
    cnt = 0
    queue = deque([start])
    if start == 0:
        visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i == 0 and not visited[i]:
                visited[i] = True
                queue.append(i)
        cnt += 1
    return cnt


cnt = bfs(case, 0, visited)
print(cnt)
