# 41

# 메모리초과
from itertools import combinations

n = int(input())
nums = sorted(map(int, input().split()))
s = set()

for i in nums:
    s.add(i)

for i in range(2, n):
    lst = list(combinations(nums, i))
    for i in lst:
        s.add(sum(i))

l = sorted(s)

for i in range(1, len(l)):
    if l[i] != l[i - 1] + 1:
        print(l[i - 1] + 1)
        break

############################################################

n, a = int(input()), sorted(map(int, input().split()))
ans = 0 # 만들 수 있는 최소값

for i in a:
    if i <= ans + 1:
        ans += i
    else:
        break

print(ans + 1)
