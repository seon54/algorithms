import sys

input = sys.stdin.readline
D, N = map(int,input().split())
oven = list(map(int,input().split()))
pizza = list(map(int,input().split()))
idx = 0

# oven[i] 가 oven[i - 1]보다 크다면 그 값의 피자는 들어올 수 없으므로 둘 중 작은 값으로 할당한다
for i in range(1, D):
    oven[i] = min(oven[i - 1], oven[i])

for i in reversed(range(D)):
    # 오븐이 피자보다 크거나 같을 때 넣을 수 있다
    if pizza[idx] <= oven[i]:
        idx += 1

    if idx == N:
        # 위치를 출력해야 하므로 인덱스 값에 1을 더한다
        print(i + 1)
        exit(0)

print(0)