def solution(n):
    if n < 3:
        return n
    
    answer = 0
    temp = []

    while n >= 3:
        d, v = divmod(n, 3)
        temp.insert(0, str(v))

        if d < 3:
            temp.insert(0, str(d))
            break
        n = d
    n = int(''.join(temp[::-1]))
    cnt = 0
    while n:
        answer += (3 ** cnt) * (n % 10)
        n //= 10      
        cnt += 1

    return answer

######################################################

def solution(n):
    answer = 0
    cnt = 1
    a = ''

    while n:
        a+=str(n%3)
        n = n//3

    for i in range(len(a) - 1, -1, -1):
        answer += int(a[i]) * cnt
        cnt *= 3
    return answer

######################################################

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

######################################################

def solution(n):
    answer = 0
    cnt = 1
    temp = ''
    
    while n:
        temp += str(n % 3)
        n //= 3
        
    for i in temp[::-1]:
        answer += int(i) * cnt
        cnt *= 3
    return answer