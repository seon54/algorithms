from collections import Counter
import sys


n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
c = Counter(cards)
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for num in nums:
    print(c[num], end=' ')