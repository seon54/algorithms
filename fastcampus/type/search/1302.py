"""
08. 기본 탐색 알고리즘
난이도: 하
유형: 탐색
추천 풀이 시간: 20분

김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 
김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.
오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 
이 값은 1,000보다 작거나 같은 자연수이다. 
둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 
책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.

[출력]
첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 
만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.
"""
n = int(input())
d = dict()
max_value = 0
array = []

for _ in range(n):
    book = input()
    if book in d:
        d[book] += 1        
    else:
        d[book] = 1

for i in d.values():
    if i > max_value:
        max_value = i

for k, v in d.items():
    if v == max_value:
        array.append(k)

array.sort()
print(array[0])

######################################################

n = int(input())
books = dict()

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

target = max(books.values())
array = []

for book, number in books.items():
    if number == target:
        array.append(number)

print(sorted(array)[0])