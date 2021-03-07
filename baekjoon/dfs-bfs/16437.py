import sys


sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]
sheep = [0] * (n + 1)

for i in range(2, n + 1):
    t, a, p = input().split()
    a, p = int(a), int(p)
    
    adj[p].append(i)

    if t == 'S':
        sheep[i] += a
    else:
        sheep[i] -= a


def dfs(idx):
    tmp = sheep[idx]

    for v in adj[idx]:
        tmp += dfs(v)

    return max(0, tmp)

print(dfs(1))