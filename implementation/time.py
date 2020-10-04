"""
정수 N이 되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하시오

입력 조건
- 첫째 줄에 정수 N이 입력된다 (0 <= N <= 23)

출력 조건
- 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수 출력
"""

# 내 풀이
n = int(input())

cnt = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(k) or '3' in str(j) or '3' in str(i):
                cnt += 1

print(cnt)

# 풀이
h = int(input())

cnt = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(i):
                cnt += 1

print(cnt)
