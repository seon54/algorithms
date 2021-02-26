n, m = map(int, input().split())
d = dict()
for _ in range(n):
    team, num = input().strip(), int(input())
    d[team] = list()

    for _ in range(num):
        d[team].append(input().strip())

for _ in range(m):
    name = input().strip()
    num = int(input())

    if num == 0:
        for member in sorted(d[name]):
            print(member)
    else:
        for k, v in d.items():
            if name in v:
                print(k)

############################################################

N, M = map(int, input().split())

team_mem, mem_team = {}, {}

for i in range(N):
    team_name, mem_num = input(), int(input())
    team_mem[team_name] = []
    for j in range(mem_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for i in range(M):
    name, q = input(), int(input())

    if q:
        print(mem_team[name])
    else:
        for mem in sorted(team_mem[name]):
            print(mem)