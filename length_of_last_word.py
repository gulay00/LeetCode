# LeetCode - Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.split()
        return len(s1[-1])
