from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}

        for x in nums:
            counts[x] = counts.get(x, 0) + 1

        for key, value in counts.items():
            if value == 1:
                return key
