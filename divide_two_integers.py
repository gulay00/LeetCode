# LeetCode - Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Special overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        d = dividend / divisor
        return int(d)
