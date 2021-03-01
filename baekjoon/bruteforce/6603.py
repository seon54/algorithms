from itertools import combinations

while True:
    t = list(map(int, input().split()))

    if t[0] == 0:
        break

    for i in sorted(combinations(t[1:], 6)):
        print(*i)
    print()