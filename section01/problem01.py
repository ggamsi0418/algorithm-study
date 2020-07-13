"""
    1. Two Sum
    
    (https://leetcode.com/problems/two-sum/)
"""


class Solution(object):
    def twoSum(self, nums, target):
        list_length = len(nums)

        for i, value_a in enumerate(nums):
            for j in range(i + 1, list_length):
                value_b = nums[j]
                if value_a + value_b == target:
                    return [i, j]


# class Solution(object):
#     def twoSum(self, nums, target):
#         list_length = len(nums)

#         for i, value_a in enumerate(nums):
#             value_b = target - value_a

#             try:
#                 j = nums.index(value_b, i + 1, list_length)
#             except ValueError:
#                 j = -1

#             if j != -1 and j != i:
#                 return [i, j]


sol = Solution()
print(sol.twoSum([3, 3], 6))

