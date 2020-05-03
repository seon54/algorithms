"""
N명의 학생의 수학성적이 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.
답이 2개일 경우 성적이 높은 학생의 번호를 출력하세요. 만약 답이 되는 점수가 여러 개일
경우 번호가 빠른 학생의 번호를 답으로 한다.

첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 N개의 자연수가 주어진다.
학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
평균은 소수 첫째 자리에서 반올림합니다.
"""

# 내 풀이

n = int(input())
l = list(map(int, input().split()))

avg = int(round(sum(l) / len(l), 0))
results = {}

for i, v in enumerate(l):
    results[v] = abs(avg-v)
print(results)
min_value = min(list(results.values()))
key_list = []

for k, v in results.items():
    if v == min_value:
        key_list.append(k)

length = len(key_list)

if length == 1:
    print(avg, l.index(key_list[0])+1)
elif length == 2:
    print(avg, l.index(max(key_list))+1)
else:
    num = []
    for i in key_list:
        num.append(l.index(i))
    print(avg, min(num)+1)


# 강의 내용

n = int(input())
a = list(map(int, input().split()))
avg = round(sum(a) / n)
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x - avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(avg, res)
