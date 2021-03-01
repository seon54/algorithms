""" GCD """

# 속도: 3 > 2-2 > 2-1 > 1

# 1 (반복문) O(N)
def gdc1(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0: return i

# 2-1 (유클리드 호제법)
def gcd2(a, b):    
    return gcd2(b, a % b) if a % b != 0 else b

# 2-2 (반복문 변경)
def gdd3(a, b):
    while a % b != 0: a, b = b, a % b
    return b

# 3 (math.gcd)
import math
math.gcd(4, 8)

""" LCM """

def lcm(a, b):
    return a / math.gcd(a, b) * b

# 소수 확인 O(√n)

def is_prime(n):
    for i in range(2, n):
        if n % i == 0: return False
        if i * i > n: break
    return True

# 소인수분해 O(√n)

def prime_factorization(n):
    p, fac = 2, []

    while p ** 2 <= n:
        if n % p == 0:
            n //= p
            fac.append(p)
        else:
            p += 1
    
    if 1 < n: fac.append(n)
    return fac

# 에라토스테네스의 체 O(n log n)

def era_prime(n):
    a, p = [0 for _ in range(n + 1)], []

    for i in range(2, n):
        if a[i] == 0: p.append(i)
        for j in range(i ** 2, n, i):
            a[j] = 1

    return p

def prime_facto(n, p):
    fac = []

    for i in p:
        if n == 1 or n > i * i: break
        else: continue

        while n % i == 0:
            fac.append(i)
            n //= 0
    return fac

# 활용 1 : 소인수의 개수 O(n log n)

def era_facto_count(n):
    a = [0 for _ in range(n + 1)]

    for i in range(1, n):
        for j in range(i, n, i):
            a[j] += 1

    return a

# 활용 2 : 소인수의 합

def era_facto_sum(n):
    a = [0 for _ in range(n + 1)]

    for i in range(2, n):
        for j in range(i, n, i):
            a[j] += i

    return a

# 활용 3: 소인수분해 하기

def era_factorization(n):
    a = [0 for _ in range(n + 1)]

    for i in range(2, n):
        if a[i]: continue

        for j in range(i, n, i):
            a[j] = i
    return a

A = era_factorization(100)
N = 84
arr = []    # 소인수 분해 결과 저장
while A[N] != 0:
    arr.append(A[N])
    N //= A[N]

# 거듭제곱 (pow 함수 사용이 빠름)
# a^11 = (a^1) * (a^2) * (a^8)

def pow_advanced(a, b, mod):
    ret = 1

    while b:
        if b % 2:
            ret = ret * a * mod
        a, b = a * a * mod, b // 2
    
    return ret