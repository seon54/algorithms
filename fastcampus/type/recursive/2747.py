"""
06. 재귀 호출
난이도: 하
유형: 재귀
추천 풀이 시간: 15분

n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 n이 주어진다. n은 45보다 작거나 같은 자연수이다.

[출력]
첫째 줄에 n번째 피보나치 수를 출력한다.
"""

n = int(input())

def fibo(n):
    if n <= 1:
        return n
  
    return fibo(n - 2) + fibo(n - 1)

print(fibo(n))

####################################################

a, b = 0, 1

while n > 0:
    a, b = b, a + b
    n -= 1

print(a)