"""
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는
프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력
한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하
여 프로그래밍 한다.

첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 100,000를 넘지 않는다.
"""

# 내 풀이


def reverse(x):
    return int(x[::-1])


def isPrime(x):
    result = False

    if x == 1:
        return result

    for i in range(2, x):
        if x % i != 0:
            result = True
        else:
            result = False
            break

    return result


n = int(input())
nums = list(map(reverse, input().split()))

for num in nums:
    if isPrime(num):
        print(num, end=' ')

# 수업 내용

n = int(input())
a = map(int, input().split())


def reverse(x):
    res = 0

    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10


def isPrime(x):
    if x == 1:
        return False

    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True


for num in a:
    tmp = reverse(num)
    if isPrime(tmp):
        print(tmp, end=' ')
