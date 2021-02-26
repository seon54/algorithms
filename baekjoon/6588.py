import math
import sys


def prime(n):
    array = [True for _ in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i]:
            j = 2

            while i * j <= n:
                array[i * j] = False
                j += 1

    return array

nums = []

while True:
    n = int(sys.stdin.readline())
    
    if n == 0:
        break

    nums.append(n)

prime_nums = prime(max(nums))

for n in nums:
    
    for i in range(2, len(prime_nums)):

        if prime_nums[i] and prime_nums[n - i]:
            print(f'{n} = {i} + {n-i}')
            break     

    else:
        print("Goldbach's conjecture is wrong.")
