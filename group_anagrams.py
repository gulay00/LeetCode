from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together from a list of strings.

        Approach:
            For each string, build a frequency count of 26 letters.
            Use that count (as a tuple) as a dictionary key to group anagrams.

        Args:
            strs: List of lowercase English strings.

        Returns:
            A list of grouped anagram lists.

        Time Complexity:  O(n * k)  — n = number of strings, k = max string length
        Space Complexity: O(n * k)  — storing all strings in the hash map
        """
        d = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1

            d[tuple(count)].append(s)

        return list(d.values())


# ── Quick smoke test ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]

    for i, (inp, expected) in enumerate(test_cases):
        result = sol.groupAnagrams(inp)
        # Sort inner lists and outer list for order-independent comparison
        result_sorted   = sorted(sorted(g) for g in result)
        expected_sorted = sorted(sorted(g) for g in expected)
        status = "PASS" if result_sorted == expected_sorted else "FAIL"
        print(f"Test {i + 1}: {status}  →  {result}")
