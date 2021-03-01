#  40

# 풀이 실패 (0일 때 처리 안 함)
m = int(input())

if m:
    cnt = len(str(m))

    if int('1' * cnt) <= m:
        print(cnt)
    else:
        print(cnt - 1)
else:
    print(1)

# 답
n = input()
s = '1' * len(n)

if int(s) <= int(n):
    print(len(n))
else:
    print(len(n) - 1)