# 39

s = input().rstrip()
d = {'0': 0, '1': 0}
i = 0

while i < len(s):
    if i <len(s) and s[i] == '0':
        d['0'] += 1
        
        while i < len(s) and s[i] != '1':
            i += 1

    if i < len(s) and s[i] == '1':
        d['1'] += 1

        while i < len(s) and s[i] != '0':
            i += 1

print(min(d.values()))

"""
(길이, 바뀌는 구간 수)
0 1 : 0, 0  
01 10 : 1, 1
101 010 : 1, 2
1010 : 2, 3
10101 01010 : 2, 4
101010 010101 : 3, 5

=> 규칙성 찾기 -> (바뀌는 구간 + 1) / 2
"""

S, tot = input(), 0

for i in range(1, len(s)):
    if S[i] != S[i - 1]: tot += 1

print((tot + 1) // 2)
