"""
체스판은 8x8 좌표 평면이며 나이트는 이동할 때는 L자 형태로만 이동할 수 있으며 밖으로 나갈 수 없다.
나이트는 특정한 위치에서 2가지 경우로 이동할 수 있다.
    1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
    2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
행 위치를 표현할 때는 1부터 8까지 표현하며, 열 위치를 표현할 때는 a부터 h로 표현한다.
나이트의 위치가 주어졌을 때 이동할 수 있는 경우의 수를 출력하라.

입력 조건
- 첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
    입력 문자는 a1처럼 열과 행으로 이뤄진다.

출력 조건
- 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.
"""

# 내 풀이
x, y = input()
x_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
x = x_values[x]
y = int(y)
cnt = 0

if x > 2:
    if y > 2:
        cnt += 8
    elif y == 2:
        cnt += 6
    else:
        cnt += 4
elif x == 2:
    if y > 2:
        cnt += 6
    else:
        cnt += 3
else:
    if y > 2:
        cnt += 4
    else:
        cnt += 2

print(cnt)

# 풀이
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)
