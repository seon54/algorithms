c1, m1 = map(int, input().split())
c2, m2 = map(int, input().split())
c3, m3 = map(int, input().split())

def first(m1, m2, c2):    
    if m1 + m2 <= c2:
        m2 += m1
        m1 = 0
    else:
        m1 -= (c2 - m2)
        m2 = c2
    
    return m1, m2
        

def second(m2, m3, c3):
    if m2 + m3 <= c3:
        m3 += m2
        m2 = 0
    else:
        m2 -= (c3 - m3)
        m3 = c3

    return m2, m3


def third(m3, m1, c1):
    if m3 + m1 <= c1:
        m1 += m3
        m3 = 0
    else:
        m3 -= (c1 - m1)
        m1 = c1

    return m1, m3

cnt = 0
while cnt < 100:

    m1, m2 = first(m1, m2, c2)
    cnt += 1

    if cnt == 100:
        print(m1)
        print(m2)
        print(m3)
        break

    m2, m3 =second(m2, m3, c3)
    cnt += 1
    m1, m3 = third(m3, m1, c1)
    cnt += 1

##################################################################

C, M = [0, 0, 0], [0, 0, 0]

for i in range(3):
    C[i], M[i] = map(int, input().split())

for i in range(100):
    idx, nxt = i % 3, (i + 1) % 3
    M[idx], M[nxt] = max(M[idx] - (C[nxt] - M[nxt]), 0), min(C[nxt], M[nxt] + M[idx])

for i in M:
    print(i)