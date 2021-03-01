# 43  탐욕법 중 가장 어려운 유형
# 힙 활용

import copy
import heapq


K, N = map(int, input().split())
p_list = list(map(int, input().split()))
lst, ck = copy.deepcopy(p_list), set()

heapq.heapify(lst)
ith = 0

while ith < N:
    min_ = heapq.heappop(lst)
    if min_ in ck:
        continue
    ith += 1
    ck.add(min_)
    for i in p_list:
        if min_ * i < 2 ** 32:
            heapq.heappush(lst, min_ * i)

print(min_)
