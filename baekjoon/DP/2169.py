n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1000000] * m for _ in range(n)]
left = [[-1000000] * m for _ in range(n)]
right = [[-1000000] * m for _ in range(n)]

dp[0][0] = arr[0][0]

# 첫번째 줄은 오른쪽으로만 이동하는 경우로 값 채우기
for j in range(1, m):
    dp[0][j] = dp[0][j - 1] + arr[0][j]

for i in range(1, n):

    ## 왼쪽에서 오른쪽으로 이동할 때
    
    # 위줄의 값과 현재 값 더하기
    left[i][0] = dp[i - 1][0] + arr[i][0]

    for j in range(1, m):   # 위에서 0번째를 채웠으므로 1 ~ m-1 까지 채운다
        left[i][j] = max(dp[i - 1][j], left[i][j - 1])  + arr[i][j]

    ## 오른쪽에서 왼쪽으로 이동할 때

    # 윗줄의 값과 현재 위치 값 더하기
    right[i][m - 1] = dp[i - 1][m - 1] + arr[i][m - 1]
    
    for j in range(m - 2, -1, -1):  # 위에서 m-1번째를 채웠으므로 m-2 ~ 0까지 채운다
        right[i][j] = max(dp[i - 1][j], right[i][j + 1]) + arr[i][j]

    # 합치기
    for j in range(m):
        dp[i][j] = max(right[i][j], left[i][j])

print(dp[n - 1][m - 1])
