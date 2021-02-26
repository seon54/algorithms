import string

def solution(new_id):    
    answer = ''

    for c in new_id.lower():
        if c in string.ascii_lowercase or c in string.digits or c in ['-', '_', '.']:
            answer += c

    while True:
        answer = answer.replace('..', '.')
        if answer.find('..') == -1:
            break

    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]

    if not answer:
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]

        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]            

    return answer

test = "abcdefghijklmn.p"

print(solution(test))