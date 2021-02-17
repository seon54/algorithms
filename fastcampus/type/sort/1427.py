"""
04 - 기본 정렬 알고리즘
난이도: 하
유형: 정렬, 배열
추천 풀이 시간: 25분

배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

[입력]
첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

[출력]
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
"""

n = int(input())
l = list()
result = 0

while True:
    if n > 10:
        l.append(n % 10)
        n //= 10
    else:
        l.append(n)
        break

l.sort(reverse=True)

for i in range(len(l)):
    result += l[i] * pow(10, len(l) - 1 - i)

print(result)

############################################################

array = input()

for i in range(9, -1, -1):
    for j in array:
        if int(j) == i:
            print(i, end='')