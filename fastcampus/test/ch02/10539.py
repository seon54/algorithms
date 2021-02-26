n = int(input())
lst = list(map(int, input().split()))
result = [lst[0]]

for i in range(1, n):
    x = lst[i] * (i + 1) - sum(result)
    result.append(x)

print(' '.join(map(str, result)))

##################################################

N, B = int(input()), list(map(int, input().split()))

A = [B[0]]

for i in range(1, N):
    A.append(B[i] * (i + 1) - sum(A))

for i in A: print(i, end=' ')
