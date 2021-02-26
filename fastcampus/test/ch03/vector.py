"""
    N   S   E   W
x   -1  1   0   0
y    0  0   1   -1  

* 사용 편리 (NSEW)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

* 반시계 방향 (ENWS)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

* 시계 방향 (ESWN)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
"""

way = input()
x, y = 0, 0
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

x += dx['NSEW'.index(way)]
y += dy['NSEW'.index(way)]

# dfs 에서 활용

def dfs():
    pass


for i in range(4):
    dfs(x + dx[i], y + dy[i])