"""
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
제한시간은 1초입니다.

첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.

첫 줄에 소수의 개수를 출력합니다.
"""

# 내 풀이

n = int(input())
prime_nums = [2, 3, 5, 7]
cnt = 0

if n <= 10:

    for num in prime_nums:
        if n >= num:
            cnt += 1

elif 10 < n <= 100:

    for i in range(10, 101):
        is_prime = False
        for num in prime_nums:
            if i % num == 0:
                is_prime = False
                break
            else:
                is_prime = True

        if is_prime:
            prime_nums.append(i)

    cnt = len(prime_nums)

else:

    for i in range(10, 101):
        is_prime = False
        for num in prime_nums:
            if i % num == 0:
                is_prime = False
                break
            else:
                is_prime = True

        if is_prime:
            prime_nums.append(i)

    print(prime_nums)

    for i in range(101, n+1):
        is_prime = False
        for num in prime_nums:
            if i % num == 0:
                is_prime = False
                break
            else:
                is_prime = True

        if is_prime:
            prime_nums.append(i)

    cnt = len(prime_nums)

print(cnt)

# 강의 내용

n = int(input())
a = [0] * (n+1)

for i in range(2, n+1):
    if a[i] == 0:
        cnt += 1

    for j in range(i, n+1, i):
        a[j] = 1

print(cnt)
