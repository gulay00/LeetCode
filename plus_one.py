# LeetCode - Plus One
# https://leetcode.com/problems/plus-one/

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 1
        count = 0
        for x in digits[::-1]:
            count += x * i
            i *= 10

        count += 1
        count2 = [int(x) for x in str(count)]
        return count2
