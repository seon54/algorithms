def prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n, arr = int(input()), list(map(int, input().split()))
cnt = 0

for i in arr:
    if prime(i):
        cnt += 1

print(cnt)