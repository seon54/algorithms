S, tmp = input(), ''
check = False

for i in S:
    if i == ' ':
        if not check:
            print(tmp[::-1], end=' ')
            tmp = ''
        else:
            print(' ', end='')

    elif i == '<':
        check = True
        print(tmp[::-1] + '<', end='')
        tmp = ''

    elif i == '>':
        check = False
        print('>', end='')

    else:
        if check:
            print(i, end='')
        else:
            tmp += i

print(tmp[::-1], end=' ')

# 두번째 풀이

S, tmp = input(), ''
check = False
answer = ''

for i in S:
    if i == ' ':
        if not check:
            answer += tmp[::-1] + ' '
            tmp = ''
        else:
            answer += ''

    elif i == '<':
        check = True
        answer += tmp[::-1] + '<'
        tmp = ''

    elif i == '>':
        check = False
        answer += '>'

    else:
        if check:
            answer += i
        else:
            tmp += i

answer += tmp[::-1]
print(answer)

# 세번째 풀이

text, array, i = input().rstrip(), list(), 0

while i < len(text):
    if text[i] == '<':
        while i < len(text) and text[i] != '>':
            print(text[i], end='')
            i += 1

        if text[i] == '>':
            print(text[i], end='')
            i += 1

    else:
        while i < len(text) and text[i] != '<' and text[i] != ' ':
            array.append(text[i])
            i += 1

        while array:
            print(array.pop(), end='')

        if i < len(text) and text[i] == ' ':
            print(text[i], end='')
            i += 1
