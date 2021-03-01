from itertools import permutations


n = int(input())

for i in sorted(permutations([i for i in range(1, n + 1)], n)):
    print(*i)