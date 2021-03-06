import sys


def solve(n):
    if n <= 3: return 1

    arr = [0] * (n + 1)

    for i in range(1, 4):
        arr[i] = 1

    for i in range(4, n + 1):
        if i % 2 == 0 and i % 3 == 0:
            arr[i] = min(arr[i - 1], arr[i // 2], arr[i // 3]) + 1
        elif i % 3 == 0:
            arr[i] = min(arr[i - 1], arr[i // 3]) + 1
        elif i % 2 == 0:
            arr[i] = min(arr[i - 1], arr[i // 2]) + 1
        else:
            arr[i] = arr[i - 1] + 1

    print(list(range(n + 1)))
    print(arr)
    return arr[n]

print(solve(int(sys.stdin.readline())))

# 실패