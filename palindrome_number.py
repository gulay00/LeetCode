# LeetCode Task: Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# Example test
sol = Solution()
print(sol.isPalindrome(121))
