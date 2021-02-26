"""
[가장 많이 빈출되는 유형]
BFS, DFS, 등수조사, 조건문, 반복문
"""

# 논리연산자 / 비트연산자 활용
a, b = 10, 20

if a > b:
    if a % 10 == 0:
        print(a)

if a > b and a % 10 == 0:
    print(a)

"""
비트연산자
1 << 2, 1 & 1
1 | 1
1 ^ 1
"""

# 상태를 나타내는 자료 활용하기
n = 71
ck = False
for i in range(1, n):
    if n % i == 0:
        print('not prime')
        ck = True
        break

if not ck:
    print('prime')

# 나눠서 진행하기

def is_prime(n):
    for i in range(1, n):
        if n % i == 0:
            return False
    return True

for n in range(10, 100):
    if is_prime(n):
        print(f'{n} is prime')
    else:
        print('not prime')

# 여러 자료구조와 메서드, 함수 활용하기

text = 'abba'

for i in text:
    if text[i] != text[len(text) - i - 1]:
        print('not palidrome')

# 시간복잡도 여유가 있을 때

if text[:] == text[::-1]:
    print('palindrome')

# 배열에 중복된 값이 없는지 확인

def is_unique(lst):
    return len(lst) == len(set(lst))

# 미리 처리한 케이스와 처리할 케이스 정리하기

# 예제, 최소, 최대, 예외, 랜덤 케이스 만들기
