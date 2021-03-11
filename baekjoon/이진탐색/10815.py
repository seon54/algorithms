import bisect
import sys

input = sys.stdin.readline

n = int(input())
cards = sorted(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))


for i in check:
    temp = bisect.bisect_left(cards, i)

    if temp == n or cards[temp] != i:
        print(0, end=' ')
    else:
        print(1, end=' ')

#######################################################

n = int(input())
nums = set(input().split())
m = int(input())
print(' '.join('1' if x in nums else '0' for x in input().split()))