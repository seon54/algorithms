# 강의 다시 듣기 (탐색 문제풀이 D)

from copy import deepcopy


n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = [tuple(map(int, input().split())) for _ in range(k)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]   #남서북동
ans = 10000

def value(arr):
    return min([sum(i) for i in arr])


def convert(arr, qr):
    r, c, s = qr
    r, c = r - 1, c - 1
    new_arr = deepcopy(arr)

    for i in range(1, s + 1):
        rr, cc = r - i, c + i
        for w in range(4):
            for d in range(i * 2):
                rrr, ccc = rr + dx[w], cc + dy[w]
                new_arr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc

    return new_arr


def dfs(arr, qr):
    global ans

    if sum(qr) == k:
        ans = min(ans, value(arr))
        return

    for i in range(k):
        if qr[i]:
            continue

        new_arr = convert(arr, q[i])

        # 백트래킹
        qr[i] = 1
        dfs(new_arr, qr)
        qr[i] = 0

 
dfs(a, [0 for i in range(k)])

print(ans)