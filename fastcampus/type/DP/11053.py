"""
12. 동적프로그래밍 - 기초 문제
난이도: 하
유형: 동적 프로그래밍, LIS(Longest Increasing Subsequence)
추천 풀이 시간: 30분
"""
n = int(input())
array = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):

        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
    