import sys


a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))
c = list(map(int, sys.stdin.readline().rstrip().split()))

result_a, result_b, result_c = [], [], []


def cal(a_list, ah_1, am_1, as_1, ah_2, am_2, as_2):
    if (as_2 - as_1) < 0:
        am_2 -= 1
        as_2 += 60
    a_list.insert(0, as_2-as_1)

    if (am_2 - am_1) < 0:
        ah_2 -= 1
        am_2 += 60
    a_list.insert(0, am_2 - am_1)

    a_list.insert(0, ah_2 - ah_1)

    return map(str, a_list)


print(' '.join(cal(result_a, *a)))
print(' '.join(cal(result_b, *b)))
print(' '.join(cal(result_c, *c)))
