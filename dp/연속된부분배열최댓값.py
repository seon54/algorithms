"""
배열 안에서 연속된 부분 배열의 최댓값

M(n) = max(M(n-1) + arr[n], arr[n])
"""

arr = [-2, -3, 4, -1, -2, 1, 5, -3]

# 완전 탐색

def brute_force(arr):
    max_sum, temp_sum = -99999999, 0

    for i in range(len(arr)):
        temp_sum = 0

        for j in range(i, len(arr)):
            temp_sum += arr[j]
            max_sum = max(max_sum, temp_sum)

    return max_sum


# 카데인 알고리즘

def kadane(arr):
    temp, mx, is_negative = 0, -99999999, True

    for i in arr:
        if i >= 0: 
            is_negative = False
            break
        elif i > mx:
            mx = i

    if is_negative: return mx

    for i in range(len(arr)):
        temp += arr[i]

        if temp < 0:
            temp = 0

        mx = max(temp, mx)

    return mx

print(kadane([-1,-2,-3]))