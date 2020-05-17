"""
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만
듭니다. 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이
됩니다. 즉 첫 자리 0은 자연수화 할 때 무시합니다. 출력은 120를 출력하고, 다음 줄에 120
의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.

첫 줄에 숫자가 썩인 문자열이 주어집니다. 문자열의 길이는 50을 넘지 않습니다.
첫 줄에 자연수를 출력하고, 두 번째 줄에 약수의 개수를 출력합니다.
"""

# 내 풀이

s = input()
nums = [str(x) for x in range(10)]
num = ''
cnt = 0

for c in s:
    if c in nums:
        num += c

num = int(num)

for i in range(1, num + 1):
    if num % i == 0:
        cnt += 1


print(num)
print(cnt)

# 내 풀이 2

s = input()
nums = [str(x) for x in range(10)]
num = 0
cnt = 0

for c in s:
    if c in nums:

        if c == '0' and num == '':
            pass
        else:
            num = (num * 10 + int(c))

for i in range(1, num + 1):
    if num % i == 0:
        cnt += 1


print(num)
print(cnt)


# 수업 내용

s = input()
res = 0

for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)

print(res)

cnt = 0

for i in range(1, res + 1):

    if res % i == 0:
        cnt += 1

print(cnt)
