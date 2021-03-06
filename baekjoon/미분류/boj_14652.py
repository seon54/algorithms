"""
당신은 한화 이글스의 감독이다. 열혈인 욱제의 방문에 깊은 감동을 받은 당신은 욱제가 잃어버린 자리를 찾아주려고 한다. 
오늘 경기가 펼쳐지는 잠실구장은 세로 길이가 N, 가로 길이가 M인 N*M 크기의 관중석을 가지고 있다. 
관중석의 왼쪽 위는 (0, 0), 오른쪽 아래는 (N-1, M-1)으로 표시된다. 각 관중석에는 번호가 아래 그림처럼 매겨져있다. 
(0, 0)에서부터 0번으로 시작하여 오른쪽으로, 끝에 다다르면 그 아래에서 또 오른쪽으로 숫자가 증가해나가는 식이다.

첫째 줄에 관중석의 크기를 나타내는 N, M과 잃어버린 관중석 번호를 나타내는 K가 주어진다. (1 <= N, M <= 30,000, 0 <= K <= N*M-1)

욱제의 잃어버린 자리를 찾아서, 잃어버린 자리의 좌표 (n, m)를 하나의 공백을 사이에 두고 숫자만 출력한다.
"""
import sys


n, m, k = map(int, sys.stdin.readline().rstrip().split())
cnt = 0
is_finished = False


for i in range(n):
    for j in range(m):
        if cnt == k:
            print(f'{i} {j}')
            is_finished = True
            break
        cnt += 1

    if is_finished:
        break
