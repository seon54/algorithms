# bfs / dfs & 구현
# 30 - 40 분
# 최대값을 찾는 것이므로 맵의 방향을 돌려가면서 확인
# 함수 단위로 쪼개서 풀기
# 암기

from copy import deepcopy


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def convert(lst, n):
    new_list = [i for i in lst if i]
    for i in range(1, len(new_list)):
        if new_list[i - 1] == new_list[i]:
            new_list[i - 1] *= 2
            new_list[i] = 0

    new_list = [i for i in new_list if i]
    return new_list + [0] * (n - len(new_list))


# 90도 회전
def rotate(board, n):   
    nb = deepcopy(board)
    for i in range(n):
        for j in range(n):
            nb[j][n - i - 1] = board[i][j]

    return nb


def dfs(n, board, count):
    ret = max([max(i) for i in board])
    
    if count == 0:
        return ret

    for _ in range(4):  # 맵을 돌리는 횟수
        x = [convert(i, n) for i in board]
        if x != board:
            ret = max(ret, dfs(n, x, count - 1))
        board = rotate(board, n)

    return ret


print(dfs(n, board, 5))