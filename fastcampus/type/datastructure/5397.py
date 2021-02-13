"""
02. 기본자료구조 - 02. 핵심 유형 문제풀이
난이도: 중
유형: 스택, 구현, 그리디
추천 풀이 시간: 40분

창영이는 강산이의 비밀번호를 훔치기 위해서 강산이가 사용하는 컴퓨터에 키로거를 설치했다. 
며칠을 기다린 끝에 창영이는 강산이가 비밀번호 창에 입력하는 글자를 얻어냈다.
키로거는 사용자가 키보드를 누른 명령을 모두 기록한다. 
따라서, 강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다.
강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오.

[입력]
첫째 줄에 테스트 케이스의 개수가 주어진다. 
각 테스트 케이스는 한줄로 이루어져 있고, 강산이가 입력한 순서대로 길이가 L인 문자열이 주어진다. (1 ≤ L의 길이 ≤ 1,000,000) 
강산이가 백스페이스를 입력했다면, '-'가 주어진다. 이때 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지운다. 
화살표의 입력은 '<'와 '>'로 주어진다. 이때는 커서의 위치를 움직일 수 있다면, 왼쪽 또는 오른쪽으로 1만큼 움직인다. 
나머지 문자는 비밀번호의 일부이다. 물론, 나중에 백스페이스를 통해서 지울 수는 있다. 
만약 커서의 위치가 줄의 마지막이 아니라면, 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다.

[출력]
각 테스트 케이스에 대해서, 강산이의 비밀번호를 출력한다. 비밀번호의 길이는 항상 0보다 크다.
"""
import sys


n = int(sys.stdin.readline())

for _ in range(n):
    s = list(sys.stdin.readline().strip())    
    stack = []
    p = 0

    for i in range(len(s)):

        if s[i] == '<':
            if p > 0:
                p -= 1
        elif s[i] == '>':
            if p < len(stack):
                p += 1
        elif s[i] == '-':
            if p > 0:
                stack.pop(p-1)
        else:
            if p == len(stack):
                stack.append(s[i])
            else:
                stack.insert(p, s[i])
            p += 1          
        
    print(''.join(stack))


################################################################################################

for _ in range(n):
    left_stack = []
    right_stack = []
    data = input()

    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)

    # left_stack.extend(right_stack[::-1])
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))

        