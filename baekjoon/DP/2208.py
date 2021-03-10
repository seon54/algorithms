import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] * n
sum_value = 0
prefix_sum = [0]

for i in range(n):
    arr[i] = int(input())
    sum_value += arr[i]
    prefix_sum.append(sum_value)

result, temp = 0, 0

for i in range(m, n):
    temp = min(temp, prefix_sum[i - (m - 1)])
    result = max(result, prefix_sum[i + 1] - temp)

print(result)