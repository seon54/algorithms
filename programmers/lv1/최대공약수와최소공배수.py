def solution(n, m):
    answer = [0, 0]

    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            answer[0] = i

    answer[1] = answer[0] * (n // answer[0]) * (m // answer[0])
    return answer


def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1

    while t > 0:
        t = c % d
        c, d = d, t

    return [c, int(a*b/c)]