n, text = int(input()), input().strip()
cnt = 0
result = 0

for i in range(n):
    if text[i] == 'O':
        result += i + 1 + cnt
        cnt += 1
    else:
        cnt = 0

print(result)

######################################################

N, S = input(), input()
score, bonus = 0, 0

for idx, OX in enumerate(S):
    if OX == 'O':
        score, bonus = score + idx + 1 + bonus, bonus + 1
    else:
        bonus = 0

print(score)

