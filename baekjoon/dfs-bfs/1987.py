import sys

sys.setrecursionlimit(100000)

r, c = map(int, sys.stdin.readline().split())
arr = [list(map(lambda x: ord(x) - 65, input())) for _ in range(r)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
alphabet = [0] * 26
alphabet[arr[0][0]] = 1
result = 1


def dfs(a, b, cnt):
    global result, alphabet

    for i in range(4):
        x, y = a + dx[i], b + dy[i]
            
        if 0 <= x < r and 0 <= y < c and not alphabet[arr[x][y]]:                
            alphabet[arr[x][y]] = 1
            dfs(x, y, cnt + 1)
            alphabet[arr[x][y]] = 0

    result = max(cnt, result)


dfs(0, 0, 1)
print(result)