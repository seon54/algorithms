s1, s2 = input().rstrip(), input().rstrip()
n1, n2 = len(s1), len(s2)
arr = [[0] * (n2 + 1) for _ in range(n1 + 1)] 

for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        
        # 문자열의 인덱스와 맞춰주기 위해 인덱스 값에서 1 빼기
        if s1[i - 1] == s2[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

print(arr[n2][n1])