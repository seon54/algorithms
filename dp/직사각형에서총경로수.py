"""
m * n으로 구성된 직사각형에서 (0, 0)에서 (m, n)으로 가는 모든 경로의 수 구하기
이동은 오른쪽과 아래쪽만 가능
"""

# 재귀

def solve(m, n):

    if m == 0 and n == 0: return 0

    if m == 0 or n == 0: return 1

    return solve(m - 1, n) + solve(m, n - 1)

# DP


def solve_dp(m, n):
    arr = [[0] * n for _ in range(m)]

    for i in range(1, m):
        arr[i][0] = 1

    for i in range(1, n):
        arr[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

    print(arr)

    return arr[m - 1][n - 1]
