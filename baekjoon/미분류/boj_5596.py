import sys


minguk = list(map(int, sys.stdin.readline().rstrip().split()))
manse = list(map(int, sys.stdin.readline().rstrip().split()))

s = sum(minguk)
t = sum(manse)

if s != t:
    print(max([s, t]))
else:
    print(s)