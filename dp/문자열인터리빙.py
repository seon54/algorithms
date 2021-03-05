"""
a, b, c ='xyz', 'abcd', 'xzbyczd' 일 때,
a와 b의 문자열을 하나씩 합친 결과가 c와 같을 경우, c는 a와 b의 인터리빙이다
"""

# 재귀

def interleaving(a, b, c):

    if len(a) == 0 and len(b) == 0 and len(c) == 0: return True

    if len(a) + len(b) != len(c): return False

    case_a, case_b = False, False

    if a and c[0] == a[0]:
        
        case_a = interleaving(a[1:], b, c[1:])
    
    
    if b and c[0] == b[0]:
        case_b = interleaving(a, b[1:], c[1:])

    return case_a or case_b


print(interleaving('abc', '123', 'a1b2c3'))
print(interleaving('abc', '123', 'a2bcd'))

# DP

def dp_inteleaving(a, b, c):
    m, n, l = len(a), len(b), len(c)

    if m + n != l: return False

    arr = [[True] * (n + 1) for _ in range(m + 1)]

    # 첫번째 열 채우기
    for i in range(1, m + 1):
        if a[i - 1] != c[i - 1]:
            arr[i][0] = False
        else:
            arr[i][0] = True

    # 첫번째 행 채우기
    for i in range(1, n + 1):
        if b[i - 1] != c[i - 1]:
            arr[0][i] = False
        else: 
            arr[0][i] = True

    # 나머지 칸 채우기
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            current_a = a[i - 1]
            current_b = b[j - 1]
            current_c = c[i + j - 1]

            #  c가 a와 같고 b와 다를 때
            if current_a == current_c and current_b != current_c:
                arr[i][j] = arr[i - 1][j]

            #  c가 b와 같고 a와 다를 때
            elif current_a != current_c and current_b == current_c:
                arr[i][j] = arr[i][j - 1]

            # a, b, c 모두 같을 때
            elif current_a == current_b == current_c:
                arr[i][j] = arr[i - 1][j] or arr[i][j - 1]

            else:
                arr[i][j] = False

    return arr[m][n]