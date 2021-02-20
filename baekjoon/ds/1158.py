from collections import deque


n, k = map(int, input().split())
d = deque([i for i in range(1, n + 1)])
result = []

while d:
    cnt = 1

    while cnt <= k - 1:
        x = d.popleft()
        d.append(x)
        cnt += 1

    x = d.popleft()
    result.append(x)

print('<', end='')
for i in range(n):

    if i != n - 1:
        print(result[i], end=', ')
    else:
        print(result[i], end='>')
    
############################################################

array = deque(range(1, n + 1))
result = []

while array:

    for i in range(k):
        x = array.popleft()
        if i != k - 1:
            array.append(x)
        else:
            result.append(x)

print(f"<{', '.join(map(str, result))}>")

############################################################

array = list(range(1, n + 1))
result = []
index = 0

for _ in range(n):
    index += k - 1
    if index >= len(array):
        index %= len(array)
    result.append(str(array.pop(index)))
    
print(f"<{', '.join(result)}>")