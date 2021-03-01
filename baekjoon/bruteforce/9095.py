from itertools import product

nums = [1, 2, 3]
t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 1
    test = []

    for i in range(1, n):

        test += sorted(product(nums, repeat=i))

    for i in test:
        if sum(i) == n:
            cnt += 1

    print(cnt)