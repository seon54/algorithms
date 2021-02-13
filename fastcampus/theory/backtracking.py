# N Queen

def is_available(col_candidate: list, col:int):
    current_row = len(col_candidate)
    
    # 수직 체크 & 대각선 체크

    for queen_row in range(current_row):
        if col_candidate[queen_row] == col:
            return False
        if abs(col_candidate[queen_row] - col) == current_row - queen_row:
            return False

    return True


def dfs(n: int, current_row: int, col_candidate: list, result: list):
    if current_row == n:
        result.append(col_candidate[:])
        return
    
    for col in range(n):    # 각 열을 확인
        if is_available(col_candidate, col):
            col_candidate.append(col)
            dfs(n, current_row + 1, col_candidate, result)
            col_candidate.pop()     # backtrack


def solve(n):
    result = []
    dfs(n, 0, [], result)
    return result


result = solve(4)
print(result)