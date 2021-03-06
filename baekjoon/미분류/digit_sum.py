"""
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를
꼭 작성해서 프로그래밍 하세요.

첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 10,000,000를 넘지 않는다.

자릿수의 합이 최대인 자연수를 출력한다.
"""

# 내 풀이

n = int(input())
nums = map(int, input().split())


def digit_sum(x):
    x_list = list(map(int, [i for i in str(x)]))
    return sum(x_list)


max = -2147000000
result = 0

for num in nums:

    if digit_sum(num) > max:
        max = digit_sum(num)
        result = num

print(result)

# 강의 내용

n = int(input())
nums = map(int, input().split())


def digit_sum(x):
    sum = 0

    while x > 0:
        sum += x % 10
        x = x // 10

    return sum


max = -2147000000

for num in nums:
    tot = digit_sum(num)

    if tot > max:
        max = tot
        res = num

print(res)
