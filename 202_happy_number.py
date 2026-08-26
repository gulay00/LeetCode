class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            sm = 0
            while n > 0:
                sm += (n % 10) * (n % 10)
                n = n // 10
            n = sm
        return True
