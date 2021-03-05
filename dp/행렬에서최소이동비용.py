"""
** (i, j) 에서는 (i, j+1) 또는 (i + 1, j) 로만 이동 가능

"""

arr = [
    [1, 3, 5, 8],
    [4, 2, 1, 7],
    [4, 3, 2, 3]
]

# 재귀

def recursive_solution(i, j):
    # (0, 0)에서 (i, j)까지 가는 최소 비용

    if i == 0 and j == 0:
        return arr[i][j]

    if i == 0:
        return recursive_solution(0, j - 1) + arr[0][j]

    if j == 0:
        return recursive_solution(i - 1, 0) + arr[i][0]

    x = recursive_solution(i - 1, j)
    y = recursive_solution(i, j - 1)

    return min(x, y) + arr[i][j]

# 메모이재이션

memo = [[0] * 4 for _ in range(3)]

def memo_solution(i, j):

    if memo[i][j]:
        return memo[i][j]

    if i == 0 and j == 0:
        memo[i][j] = arr[i][j]

    elif i == 0:
        memo[i][j] = memo_solution(0, j - 1) + arr[0][j]

    elif j == 0:
        memo[i][j] = memo_solution(i - 1, 0) + arr[i][0]

    else:
        x = memo_solution(i - 1, j) 
        y = memo_solution(i, j - 1)

        memo[i][j] = min(x, y) + arr[i][j]

    return memo[i][j]

# 상향식

m, n = 3, 4
memo2 = [[0] * n for _ in range(m)]

def dp_solution(a, b):
    global memo2
    memo2[0][0] = arr[0][0]
    
    # 위의 행 채우기 (누적합)
    for k in range(1, n):
        memo2[0][k] = memo2[0][k - 1] + arr[0][k]
        print(k)

    # 왼쪽 행 채우기
    for k in range(1, m):
        memo2[k][0] = memo2[k - 1][0] + arr[k][0]

    # 나머지 셀 채우기
    for i in range(1, m):
        for j in range(1, n):
            memo2[i][j] = min(memo2[i - 1][j], memo2[i][j - 1]) + arr[i][j]

dp_solution(2, 3)
print(memo2)
    