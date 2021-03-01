from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = sorted(permutations(arr, m))

for i in range(len(result)):
    result[i] = sorted(result[i])

temp = []

for i in result:
    if i not in temp:
        temp.append(i)

for i in temp:
    print(*i)

######################################################

from itertools import combinations

n, m = map(int, input().split())
arr = sorted(map(int, input().split())) # 정렬 해줘야 함

for i in sorted(combinations(arr, m)):
    print(*i)