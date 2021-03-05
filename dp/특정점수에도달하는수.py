"""
한 번에 3점 또는 5점 또는 10점을 얻을 수 있는 게임이 있을 때,
플레이어가 n점에 도달하는 전체 경우의 수
"""

# 재귀

def recursive_solution(n):

    if n < 0: return 0
    if n == 0: return 1

    return recursive_solution(n - 10) + recursive_solution(n - 5) + recursive_solution(n - 3)

# dp

def dp(n):

    # memo[i]: i점에 도달하는 경우의 수
    memo = [0] * (n + 1)
    memo[0] = 1

    for i in range(1, n + 1):
        if 3 <= i:
            memo[i] += memo[i - 3]

        if 5 <= i:
            memo[i] += memo[i - 5]

        if 10 <= i:
            memo[i] += memo[i - 10]

    return memo[n]