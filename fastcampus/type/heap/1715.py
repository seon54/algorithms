"""
11. 고급 탐색 알고리즘 - 핵심 유형
제목: 카드 정렬
난이도: 하
유형: 힙, 자료구조, 그리디
추천 풀이 시간: 20분
"""
import heapq


n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    heapq.heappush(heap, x)
    
result = 0

while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    sum_ = first + second
    result += sum_    
    heapq.heappush(heap, sum_)

print(result)
