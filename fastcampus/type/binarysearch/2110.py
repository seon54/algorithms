"""
09. 기본 탐색 알고리즘
난이도: 중
유형: 이진 탐색
추천 풀이 시간: 40분

- 집의 좌표 최대 1,000,000,000  -> 탐색 범위가 넓을 때 이진탐색 고려
- 이진 탐색 O(N * logX)  [N: 집의 개수, X: 집의 좌표]
- 이진 탐색으로 최대 gap 찾기
- min, max 설정 후 중간 값 찾기 => 반복
"""
n, c = list(map(int, input().split(' ')))
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()

min_ = array[1] - array[0]      # gap의 최소값
max_ = array[-1] - array[0]     # gap의 최대값
result = 0

while (min_ <= max_):
    mid = (min_ + max_) // 2    # gap 중간값 (매번 바뀌기 때문에 while 안에 있어야 함)
    value = array[0]            # gap 을 계산하기 위한 기준점 초기화
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
