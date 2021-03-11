import sys

input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 열별로 sum한 매트릭스 따로 만들어주기 
for i in range(N):
    for j in range(1, N):        
        matrix[i][j] += matrix[i][j - 1] 

# 행별 합 출력
for _ in range(M):
    i, j, x, y = map(int, sys.stdin.readline().split())
    answer = 0

    for k in range(i - 1, x):

        # 0번 인덱스가 아니면 그 뒤 인덱스 값 빼기 (인덱스 값이므로 1을 더 빼줘서 -2가 됨)
        if j != 1:            
            answer -= matrix[k][j - 2]

        answer += matrix[k][y - 1]

    print(answer)

########################################################################################

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        DP[i][j] = DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1] + MAP[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1])