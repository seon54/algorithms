# 42

n, m  = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]
cnt = 0


def change(x, y):
    for i in range(3):
        for j in range(3):            
            a[x + i][y + j] ^= 1


for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j] and i + 2 < n and j + 2 < m:
            change(i, j)
            cnt += 1

if cnt:
    print(cnt)
else:
    print(-1)

"""
XOR(둘 중 하나만 참일 때 만족)  연산 활용
0 ^ 1 = 1
"""


N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]
ans = 0


def flip(x, y):
    for i in range(3):
        for j in range(3):
            A[x + i][y + j] ^= 1


for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            flip(i, j)
            ans += 1

print(ans if A == B else -1)