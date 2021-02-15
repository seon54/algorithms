"""
07. 고급 정렬 알고리즘 (병합, 퀵, 힙)  
난이도: 중
유형: 정렬
추천 풀이 시간: 25분

** 퀵 정렬은 최악의 경우 n^2 나올 수 있음

수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 
앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.
둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)

[출력]
A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.
"""


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

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array


n, k = list(map(int, input().split(' ')))
array = list(map(int, input().split(' ')))

array = merge(array)

print(array)
print(array[k - 1])