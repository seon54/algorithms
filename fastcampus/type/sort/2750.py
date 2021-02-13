"""
04 - 기본 정렬 알고리즘
난이도: 하
유형: 정렬
추천 풀이 시간: 15분

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

[입력]
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

[출력]
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
import sys

n = int(sys.stdin.readline())
l = list()

for _ in range(n):
    l.append(int(sys.stdin.readline()))

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if l[j] < l[min_index]:
            min_index = j
    l[min_index], l[i] = l[i], l[min_index]

for i in l:
    print(i)



