e, s, m = map(int, input().split())
a, b, c, i = 0, 0, 0, 0

while True:
    i += 1
    a += 1
    b += 1
    c += 1

    if a >= 16:
        a %= 15

    if b >= 29:
        b %= 28

    if c >= 20:
        c %= 19

    if a == e and b == s and c == m:
        break

print(i)

################################################

c = 1

while True:
    if (c-e) % 15 == 0 and (c-s) % 28 == 0 and (c-m) % 19 == 0:
        print(c)
        break
    c += 1