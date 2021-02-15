"""
08. 기본 탐색 알고리즘
난이도: 하
유형: 탐색
추천 풀이 시간: 20분
"""
def ascending(array):
    now = array[0]
    result = 1
    for i in range(1, len(array)):
        if now < array[i]:
            result += 1
            now = array[i]
    return result


n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

print(ascending(nums))
nums.reverse()
print(ascending(nums))
    