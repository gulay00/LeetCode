# LeetCode Task: Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for x in s:
            if x in "([{":                 # open bracket
                stack.append(x)
            else:                           # closing bracket
                if not stack:               # stack empty -> invalid
                    return False
                if stack[-1] != pairs[x]:   # mismatched pair
                    return False
                stack.pop()                 # valid pair -> remove

        return len(stack) == 0              # final stack must be empty
