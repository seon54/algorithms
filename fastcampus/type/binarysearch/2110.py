"""
09. 기본 탐색 알고리즘
난이도: 중
유형: 이진 탐색
추천 풀이 시간: 40분

- 이진 탐색 O(N * logX)  [X: 집의 좌표]
- 이진 탐색으로 최대 gap 찾기
- min, max 설정 후 중간 값 찾기 => 반복
"""
n, c = list(map(int, input().split(' ')))
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()

min_ = array[1] - array[0]
max_ = array[-1] - array[0]
result = 0

while (min_ <= max_):
    mid = (min_ + max_) // 2    # gap
    value = array[0]
    count = 1

    for i in range(1, len(array)):
        if mid <= array[i] - value: # 간격이 중간값보다 클 때
            value = array[i]
            count += 1
    
    if c <= count:
        min_ = mid + 1
        result = mid
    else:
        max_ = mid - 1

print(result)
