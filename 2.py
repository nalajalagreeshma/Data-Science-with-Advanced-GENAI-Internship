class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        for i in range(n):
            result.append(nums[i])       # x_i
            result.append(nums[i + n])   # y_i
        return result

# Example usage:
# sol = Solution()
# print(sol.shuffle([2,5,1,3,4,7], 3))      # Output: [2,3,5,4,1,7]
# print(sol.shuffle([1,2,3,4,4,3,2,1], 4))  # Output: [1,4,2,3,3,2,4,1]
# print(sol.shuffle([1,1,2,2], 2))          # Output: [1,2,1,2]