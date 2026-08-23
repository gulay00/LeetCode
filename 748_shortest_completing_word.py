from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        plate_count = Counter(c.lower() for c in licensePlate if c.isalpha())
        
        result = None
        for word in words:
            word_count = Counter(word)
            if all(word_count[c] >= cnt for c, cnt in plate_count.items()):
                if result is None or len(word) < len(result):
                    result = word
        
        return result
