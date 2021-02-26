n, l, k = map(int, input().split())
result, cnt = 0, 0
test = []

for _ in range(n):
    test.append(tuple(map(int, input().split())))

test.sort(key=lambda x: x[1] > l)

for s1, s2 in test:

    if cnt >= k:
        break

    if s1 <= l:
        result +=  100

    if s2 <= l:
        result += 40

    cnt += 1

print(result)
    
################################################################

N, L, K = map(int, input().split())
easy, hard = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())

    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

# hard
ans = min(hard, K) * 140

# easy
if hard < K:
    ans += min(K - hard, easy) * 100

print(ans)

    
