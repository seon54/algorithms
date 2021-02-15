"""
07. 고급 정렬 알고리즘 (병합, 퀵, 힙)  
난이도: 하
유형: 정렬
추천 풀이 시간: 20분

** 퀵 정렬은 최악의 경우 n^2 나올 수 있음

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

[입력]
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 
수는 중복되지 않는다.

[출력]
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
import sys

n = int(sys.stdin.readline())
array = []

for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()

for i in array:
    print(i)

######################################################################

import heapq

n = int(sys.stdin.readline())
array = []

for _ in range(n):
    array.append(int(sys.stdin.readline()))

heapq.heapify(array)

for i in range(len(array)):
    print(heapq.heappop(array))

######################################################################

def merge(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = merge(array[:mid])
    right = merge(array[mid:])

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    return array


n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = merge(array)

for i in array:
    print(i)
