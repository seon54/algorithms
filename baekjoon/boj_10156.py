import sys


k, n, m = map(int, sys.stdin.readline().rstrip().split())
if k * n > m:
    print(k * n - m)
else:
    print(0)
