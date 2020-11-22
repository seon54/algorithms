import sys


a, b = list(map(int, sys.stdin.readline().rstrip().split()))
c, d = list(map(int, sys.stdin.readline().rstrip().split()))

print(min([a+d, b+c]))