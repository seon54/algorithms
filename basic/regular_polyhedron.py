"""
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확
률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.

첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
"""

# 내 풀이

n, m = map(int, input().split())
d = {}

for i in range(1, n+1):
    for j in range(1, m+1):
        if d.get(i+j):
            d[i+j] += 1
        else:
            d[i+j] = 1

d = sorted(d.items(), reverse=True, key=lambda x: x[1])

num = d[0][1]

l = []

for i, j in d:
    if j == num:
        l.append(i)

l.sort()

print(*l)

# 강의 내용

n, m = map(int, input().split())
cnt = [0] * (n + m + 1)
max = -2147000000

for i in range(n+1):
    for j in range(m+1):
        cnt[i+j] += 1

for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')


# 강의 내용 수정

n, m = map(int, input().split())
cnt = [0] * (n + m + 1)
max = -2147000000

for i in range(n+1):
    for j in range(m+1):
        cnt[i+j] += 1

for v in cnt:
    if v > max:
        max = v

for i, v in enumerate(cnt):
    if v == max:
        print(i, end=' ')
