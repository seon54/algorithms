'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
'''


class Solution:
    def isValid(s):
        opened = ['(', '[', '{']
        closed = [')', ']', '}']
        stack = []
        length = len(s)

        if length == 1:
            return False
        else:
            for i in range(length):
                if s[i] in opened:
                    stack.append(s[i])
                else:
                    if not stack:
                        return False
                    else:
                        i_index = closed.index(s[i])
                        s_index = opened.index(stack[-1])
                        print(i_index, s_index)
                        if i_index == s_index:
                            stack.pop()
                        else:
                            return False
                print(stack)

        if stack:
            return True
        else:
            return False

    def isValid2(s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:

            if char in mapping:

                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack    # stack이 비어 있으면 False(return True), stack에 값이 있으면 True(return False)

    def isValid3(s):
        map = {')': '(', '}': '{', ']': '['}
        st = []
        for e in s:
            if st and (e in map and st[-1] == map[e]):
                st.pop()
            else:
                st.append(e)
        return not st