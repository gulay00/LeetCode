from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        l = [1]

        def pascal(l: List[int]) -> List[int]:
            k: List[int] = []
            for i in range(len(l) + 1):
                if i == 0 or i == len(l):
                    k.append(1)
                else:
                    k.append(l[i] + l[i - 1])
            return k

        ls: List[List[int]] = []
        for _ in range(n):
            ls.append(l)
            l = pascal(l)
        return ls
