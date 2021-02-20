"""
12. 동적프로그래밍 - 기초 문제
난이도: 하
유형: 동적 프로그래밍
추천 풀이 시간: 30분

- O(NK)
"""
n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    weight, value = map(int, input().split())

    for j in range(1, k + 1):
        if j < weight:
            # 무게가 더 작을 경우, 이전 값을 그대로 가지게 됨
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])