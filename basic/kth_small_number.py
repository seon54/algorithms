"""
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수 중
k번째로 작은 수를 출력하는 프로그램을 작성하세요.

첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어집니다.
각 케이스별
첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다.
두 번째 줄에 N개의 숫자가 차례로 주어진다.

각 케이스별 k번째 수를 아래 출력예제와 같이 출력하세요.
"""

# 풀이 실패
# 리스트 슬라이싱 후, sort() 실행해야 함

t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers = numbers[s-1:e].sort()
    print(f'#{i+1} {numbers[k-1]}')

# 수업 내용

T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print(f'#{t+1} {a[k-1]}')
