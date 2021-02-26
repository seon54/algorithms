## Flood fill


def new_array():
    return [[False for _ in range(10)] for _ in range(n)]


# 개수세기
def dfs(x, y):
    ck[x][y] = True
    ret = 1
    
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]

        if xx < 0 or xx >= n or yy < 0 or yy >= 10 or ck[xx][yy] or m[x][y] != m[xx][yy]:
            continue

        ret += dfs(xx, yy)

    return ret


# val을 0으로 채우기
def dfs2(x, y, val):
    ck2[x][y] = True
    m[x][y] = '0'

    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]

        if xx < 0 or xx >= n or yy < 0 or yy >= 10 or ck2[xx][yy] or m[xx][yy] != val:
            continue

        dfs2(xx, yy, val)


# 내리기
def down():
    for i in range(10):
        tmp = []
        for j in range(n):
            if m[j][i] != '0':
                tmp.append(m[j][i])

        for j in range(n - len(tmp)):
            m[j][i] = '0'

        for j in range(n-len(tmp), n):
            m[j][i] = tmp[j - (n - len(tmp))]


# down 보다 메모리 더 많이 사용
def down2():
    for i in range(10):
        tmp = []
        for j in range(n):
            if m[j][i] != '0':
                tmp.append(m[j][i])
                m[j][i] = '0'

        for k in range(n - 1, 0, -1):
            if tmp:
                m[k][i] = tmp.pop()


n, k = map(int, input().split())
m = [list(input()) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


while True:
    exist = False
    ck = new_array()    # 계속 갱신 되어야 함 (같은 숫자 확인)
    ck2 = new_array()   # 계속 갱신 되어야 함 (0으로 바뀌지 않은 숫자 확인)

    for i in range(n):
        for j in range(10):
            if m[i][j] == '0' or ck[i][j]:
                continue

            res = dfs(i, j) # 반환값: 총 크기

            if res >= k:
                dfs2(i, j, m[i][j])
                exist = True


    if not exist: break

    down()

for i in m:
    print(''.join(i))

