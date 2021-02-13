import random


def multiple(data):
    if data <= 1:
        return data
    return data * multiple(data - 1)



def sum(data):
    if data:
        return data.pop() + sum(data)
    
    return 0


def palindrome(text):
    print(text)
    if len(text) <= 1:
        return True

    if text[0] == text[-1]:
        return palindrome(text[1:-1])


def make_one(num):
    print(num)
    if num != 1:
        if num % 2 == 0:
            return make_one(num // 2)
        else:
            return make_one(3 * num+ 1)

    return num


def make_num(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    return make_num(num - 1) + make_num(num - 2) + make_num(num - 3)
