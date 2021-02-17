"""
11. 고급 탐색 알고리즘 - 핵심 유형
제목: 최소 힙
난이도: 하
유형: 힙, 자료구조
추천 풀이 시간: 20분
"""
# 시간초과

import sys


class Heap:

    def __init__(self):
        self.array = []

    def insert(self, data):
        if self.array and self.array[0] > data:
            self.array.insert(0, data)
            return
        
        self.array.append(data)

    def pop(self):
        if self.array:
            d = self.array.pop(0)
            if self.array:
                first = min(self.array)
                self.array.remove(first)
                self.array.insert(0, first)
            return d
        else:            
            return 0


n = int(sys.stdin.readline())
heap = Heap()
result = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heap.insert(x)
    else:
        result.append(heap.pop())

for i in result:
    print(i)

############################################################

import heapq

n = int(input())
array = []
result = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if array:
            result.append(heapq.heappop(array))
        else:
            result.append(0)
    else:
        heapq.heappush(array, x)

for data in result:
    print(data)