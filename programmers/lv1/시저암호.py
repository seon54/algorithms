def solution(s, n):
    answer = ''
    lower = list(range(97, 123))
    upper = list(range(65, 91))

    for c in s:
        if c.islower():
            index = (lower.index(ord(c)) + n) % 26
            answer += chr(lower[index])
        elif c.isupper():
            index = (upper.index(ord(c)) + n) % 26
            answer += chr(upper[index])
        else:
            answer += c
    return answer

#########################################################

def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)