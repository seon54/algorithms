"""
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을
작성하시오.

첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N
이하이다.
"""


# 내 풀이

n, k = map(int, input().split())

l = list()

for i in range(1, n+1):
    if n % i == 0:
        l.append(i)

if l:
    print(l[k-1])
else:
    print(-1)

# 수업 내용


n, k = map(int, input().split())

cnt = 0

for i in range(1, n+1):
    if n % i == 0:
        cnt += 1

    if cnt == k:
        print(i)
        break
else:
    print(-1)
