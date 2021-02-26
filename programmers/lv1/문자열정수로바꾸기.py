def solution(s):
    answer = 0
    if s[0] in ['+', '-']:
        answer += int(s[1:])
    else:
        answer += int(s)
    if s[0] == '-':
        answer *= -1
    return answer


def simple(s):
    return int(s)