# LeetCode Task: Remove Duplicates from Sorted Array

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0   # index where unique elements will be placed

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:   # found a new unique number
                i += 1
                nums[i] = nums[j]    # place it in front

        return i + 1   # number of unique elements
