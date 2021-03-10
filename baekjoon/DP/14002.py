n = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(n)]
result = [[x] for x in arr]

for i in range(n):
    for j in range(i):
        
        # 자신의 값(lst[i)보다 작고 dp 길이가 크다면 
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:            
            result[i] = arr[j] + [arr[i]]
            dp[i] = dp[j] + 1

idx, max_ = 0, 0

for i, v in enumerate(dp):
    max_ = max(max_, v)
    if v == max_: idx = i

print(idx)
print(*result(idx))


########################################################################


from bisect import bisect_left


n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
cmp = [-1000000000001]
max_ = 0

for i in range(1, n + 1):

    if cmp[-1] < arr[i]:
        cmp.append(arr[i])
        dp[i] = len(cmp) - 1
        max_ = dp[i]
    else:
        dp[i] = bisect_left(cmp, arr[i])
        cmp[dp[i]] = arr[i]

    print(f'cmp: {cmp}')
    print(f'dp: {dp}')
    print(f'max: {max_}')
    print()


res = []
for i in range(n, 0, -1):
    if dp[i] == max_:
        res.append(arr[i])
        max_ -= 1

res.reverse()
print(*res)