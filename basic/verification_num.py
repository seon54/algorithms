import sys

nums = list(map(int, sys.stdin.readline().strip().split()))

s = sum(list(map(lambda x: x*x, nums)))

print(s % 10)
