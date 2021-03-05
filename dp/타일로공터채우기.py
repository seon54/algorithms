"""
2 * n 크기의 공터를 타일로 채우기
타일의 크기는 2 * 1, 가로 또는 세로로 배치
=> 피보나치 동일
"""

# 재귀

def recursive_solution(n):

    if n == 1:
        return 1

    if n == 2:
        return 2

    return recursive_solution(n - 1) + recursive_solution(n - 2)

# dp

def dp_solution(n):
    arr = [0, 1, 2]

    for i in range(3, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])

    return arr[n]