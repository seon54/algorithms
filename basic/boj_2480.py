import sys


a, b, c = map(int, sys.stdin.readline().rstrip().split())
s = set([a, b, c])

if len(s) == 1:
    print(10000 + a * 1000)
elif len(s) == 3:
    print(max([a, b, c]) * 100)
else:
    if a == b or a == c:
        print(1000 + a * 100)
    else:
        print(1000 + b * 100)
