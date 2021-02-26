n, n_list, m, m_list = int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split()))

for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)

############################################################

# 원래는 정렬 후, 이분 탐색을 이용하여 푸는 것이 목적

N, A = int(input()), {i: 1 for i in map(int, input().split())}
M = input()
for i in list(map(int, input().split())):
    print(A.get(i, 0))