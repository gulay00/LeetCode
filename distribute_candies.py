class Solution:
    def distributeCandies(self, candyType):
        unique_types = len(set(candyType))
        max_candies = len(candyType) // 2

        return min(unique_types, max_candies)
