"""
Given a 32-bit signed integer, reverse digits of an integer.

Example. 
Input: -123
Output: -321

Input: 120
Output: 21
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            result = int(str(x)[:0:-1]) * -1
        else:
            result = int(str(x)[::-1])

        if result not in range(-(pow(2, 31), pow(2, 31))):
            return 0

        return result
