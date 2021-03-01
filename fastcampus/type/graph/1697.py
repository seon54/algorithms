"""
14. 그래프 기본 탐색 - 기초 문제
https://www.acmicpc.net/problem/1697

제목: 숨바꼭질
난이도: 하
유형: BFS
풀이 시간: 30분
"""
from collections import deque


MAX = 100001
n, k = map(int, input().split())
cnt = [0] * MAX

def bfs():
    q = deque([n])

    while q:
        node = q.popleft()

        if node == k:
            print(cnt[node])
            break

        # bfs 는 가까운 거리부터 하기 때문에  -1, +1, *2 순서로 들어가야 함
        for e in [node - 1, node + 1, node * 2]:    
            if 0 <= e < MAX and not cnt[e]:                
                cnt[e] = cnt[node] + 1
                q.append(e)               
                

bfs()
