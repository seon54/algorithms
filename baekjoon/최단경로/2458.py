import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1 # a 학생과 b 학생의 키 비교 가능하다는 의미

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b: continue

            # a와 b 사이의 학생이 있으면 a와 b도 비교 할 수 있으므로
            # graph[a][b] 의 값에 상관없이 1 을 넣어준다.
            if graph[a][k] + graph[k][b] == 2:                
                graph[a][b] = 1

cnt = [0] * n

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt[i] += 1
            cnt[j] += 1

# n - 1 : 자기 자신 제외
print(cnt.count(n - 1))
    