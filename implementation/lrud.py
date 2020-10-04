"""
입력 조건
- 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1 <= N <= 100)
- 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1 <= 이동 횟수 <= 100)

출력 조건
- 첬재 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력
"""

# 내 풀이
n = int(input())
steps = input().split()
x = y = 1

for step in steps:
    if step == 'R' and y < n:
        y += 1
    elif step == 'L' and 1 < y < n:
        y -= 1
    elif step == 'U' and 1 < x < n:
        x -= 1
    elif step == 'D' and x < n:
        x += 1

print(f'{x} {y}')

# 풀이
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plans == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
