import sys


n, k = map(int, sys.stdin.readline().split())
queue = list(range(1, n + 1))
result = []
index = 0

while queue:
    index += k - 1

    if len(queue) <= index:
        index %= len(queue)

    result.append(str(queue.pop(index)))

print(f"<{', '.join(result)}>")
