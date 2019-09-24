import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())
d = deque(range(1, n+1))
result = '<'

while d:

    for i in range(k):
        v = d.popleft()
        if i != k-1:
            d.append(v)
        else:
            if len(d) != 0:
                result += str(v) + ', '
            else:
                result += str(v)

result += '>'
sys.stdout.write(result)
