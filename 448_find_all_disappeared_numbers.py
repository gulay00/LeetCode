"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not
appear in nums.

Example:
    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [5,6]

Approach:
    Use the array itself as a hash map. For each value v = |nums[i]|,
    negate the number at index v-1 to mark it as "seen". After one pass,
    any index still holding a positive value means that index+1 never
    appeared in the array.

Time Complexity:  O(n)
Space Complexity: O(1) extra space (output array excluded)
"""


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        return [i + 1 for i in range(n) if nums[i] > 0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # [5, 6]
    print(sol.findDisappearedNumbers([1, 1]))                     # [2]
