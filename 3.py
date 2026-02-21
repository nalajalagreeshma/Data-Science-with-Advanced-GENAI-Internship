class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)  # Find the current maximum
        result = []
        for candy in candies:
            # Check if this kid would have the greatest number after extraCandies
            result.append(candy + extraCandies >= max_candies)
        return result


# Example usage:
# sol = Solution()
# print(sol.kidsWithCandies([2,3,5,1,3], 3))  # Output: [True, True, True, False, True]
# print(sol.kidsWithCandies([4,2,1,1,2], 1))  # Output: [True, False, False, False, False]
# print(sol.kidsWithCandies([12,1,12], 10))   # Output: [True, False, True]
