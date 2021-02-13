"""
03. 고급 자료구조
난이도: 하
유형: 해시, 배열, 구현
풀이 시간: 20분

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

[입력]
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.

[출력]
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""
import sys
from collections import defaultdict


n = int(sys.stdin.readline())
d = defaultdict(int)
nums = list(map(int, sys.stdin.readline().split()))

for n in nums:
    d[n] = 1

m = int(sys.stdin.readline())
nums2 = list(map(int, sys.stdin.readline().split()))

for n in nums2:
    print(d[n])

############################################################


n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i not in array:
        print('0')
    else:
        print('1')
