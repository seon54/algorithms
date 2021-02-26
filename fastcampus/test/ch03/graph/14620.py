n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 10000   # 최대값 설정

dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]  # 현재 위치 좌표 포함

# 꽃이 i, j, k에 있을 때 비용 
def check(lst):
    ret = 0         # 토지 비용
    temp = []       # 토지 크기

    for flower in lst:
        x, y = divmod(flower, n)
                
        if x in [0, n -1] or y in [0, n - 1]:
            return 10000

        for w in range(5):
            temp.append((x + dx[w], y + dy[w]))
            ret += arr[x + dx[w]][y + dy[w]]

    if len(set(temp)) != 15:    # 꽃이 겹치지 않을 때 차지하는 공간은 15
        return 10000
    return ret

# 인덱스를 하나의 숫자로 표현
for i in range(n * n):
    for j in range(i + 1, n * n):
        for k in range(j + 1, n * n):
            ans = min(ans, check([i, j, k]))

print(ans)