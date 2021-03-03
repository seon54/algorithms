"""
34. 동적계획법 - 03.문제풀이

https://www.acmicpc.net/problem/11055
가장 큰 증가 부분 수열
"""
from copy import deepcopy


n = int(input())
arr = list(map(int, input().split()))

# dp[i] : i까지 왔을 때 합의 최대
dp = deepcopy(arr)

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(arr[i] + dp[j], dp[i])
