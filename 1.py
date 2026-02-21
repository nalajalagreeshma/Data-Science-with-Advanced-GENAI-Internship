class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        total = 0
        for num in nums:
            total += num
            result.append(total)
        return result

# Example usage:
# sol = Solution()
# print(sol.runningSum([1,2,3,4]))  # Output: [1, 3, 6, 10]