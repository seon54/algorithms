"""
다양한 수로 이루어진 N 크기의 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만든다.
단, 배열의 특정 인덱스에 해당하는 수가 연속해서 K번을 초과할 수 없다.

첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분
둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000 이하의 수로 주어진다.
입력으로 주어지는 K는 항상 M보다 작거나 같다.

첫째 줄에 큰 수의 법칙에 따라 더해진 답 출력

입력 예시
5 8 3
2 4 5 4 6

출력 예시
46
"""

# 내 풀이
n, m, k = (map(int, input().split()))
list_ = list(map(int, input().split()))
list_.sort(reverse=True)
sum_ = 0

for v in list_:
    for _ in range(k):
        if m == 0:
            break
        sum_ += v
        m -= 1

# 간단 풀이
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

# 풀이
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

first_count = m // (k + 1) * k
first_count += m % (k + 1)

result += first_count * first
result += (k - first_count) * second

print(result)
