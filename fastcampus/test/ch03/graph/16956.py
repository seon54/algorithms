r, c = map(int, input().split())
array = [list(input()) for _ in range(r)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 시계방향
check = False

for i in range(r):
    for j in range(c):
        if array[i][j] == 'W':

            for w in range(4):
                ii, jj = i + dx[w], j+dy[w]

                if ii < 0 or ii == r or jj < 0 or jj == c:
                    continue

                if array[ii][jj] == 'S':
                    check = True

if check:
    print(0)
else:
    print(1)

    for i in range(r):
        for j in range(c):
            if array[i][j] not in 'SW':
                array[i][j] = 'D'

    for i in array:
        print(''.join(i))

# 다른 풀이

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
ok = True

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'W':
            for k in range(4):
                x, y = i + dx[k], j + dy[k]

                if x < 0 or x >= r or y < 0 or y >= c:
                    continue

                elif arr[x][y] == 'S':
                    ok = False

        elif arr[i][j] == '.':
            arr[i][j] = 'D'

if ok:
    print(1)
    for i in arr:
        print(''.join(i))
else:
    print(0)
