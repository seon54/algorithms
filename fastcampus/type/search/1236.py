"""
08. 기본 탐색 알고리즘
난이도: 하
유형: 탐색
추천 풀이 시간: 20분
"""
n, m = list(map(int, input().split(' ')))
array = []
cnt = 0

for _ in range(n):
    array.append(list(input()))

check_n = [0] * n
check_m = [0] * m

for i in range(len(array)):
    if 'X' in array[i]:
        check_n[i] = 1
    for j in range(len(array[i])):
        if array[i][j] == 'X':
            check_m[j] = 1

print(check_n)
print(check_m)

print(max(check_m.count(0), check_n.count(0)))

############################################################

n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(input())

row = [0] * n
column = [0] * m

for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':
            row[i] = 1
            column[j] = 1

row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1

column_count = 0
for j in range(m):
    if column[j] == 0:
        column_count += 1

print(max(row_count, column_count))
