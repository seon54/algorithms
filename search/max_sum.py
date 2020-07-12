"""
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합
니다.

첫 줄에 자연수 N이 주어진다.(1 <= N <= 50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는
다.

최대합을 출력합니다.
"""

# 내 풀이

n = int(input())
l = []

for i in range(n):
    l.append(list(map(int, input().split())))

_max = 0
_sum = 0
first_cross = 0
second_cross = 0

for inner in l:
    if sum(inner) > _max:
        _max = sum(inner)

for i in range(n):

    for j in range(n):
        _sum += l[j][i]

    if _sum > _max:
        _max = _sum

    _sum = 0

for i in range(n):
    first_cross += l[i][i]
    second_cross += l[n-i-1][i]

    if first_cross > _max:
        _max = first_cross
    elif second_cross > _max:
        _max = second_cross

print(_max)


# 수업 내용

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

largest = -2147000000

for i in range(n):
    sum_1 = sum_2 = 0

    for j in range(n):
        sum_1 += a[i][j]
        sum_2 += a[j][i]

    if sum_1 > largest:
        largest = sum_1
    if sum_2 > largest:
        largest = sum_2

sum_1 = sum_2 = 0

for i in range(n):
    sum_1 += l[i][i]
    sum_2 += l[n-i-1][i]

if sum_1 > largest:
    largest = sum_1
if sum_2 > largest:
    largest = sum_2

print(largest)
