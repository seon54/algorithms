"""
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로
그램을 작성하세요.

첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다.
두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다.
네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.
"""

# 수업 내용

n = int(input())
list_n = list(map(int, input().split()))
m = int(input())
list_m = list(map(int, input().split()))
return_list = []
p1 = p2 = 0

while p1 < n and p2 < m:
    if list_n[p1] < list_m[p2]:
        return_list.append(list_n[p1])
        p1 += 1
    else:
        return_list.append(list_m[p2])
        p2 += 1

if p1 < n:
    return_list += list_n[p1:]

if p2 < m:
    return_list += list_m[p2:]


for i in return_list:
    print(i, end=' ')
