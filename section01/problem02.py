"""
    665. Non-decreasing Array
    
    (https://leetcode.com/problems/non-decreasing-array/)
"""


class Solution(object):
    def checkPossibility(self, nums):
        nums_length = len(nums)
        cnt = 0

        for i in range(0, nums_length - 1):

            if nums[i] > nums[i + 1]:
                cnt += 1

            if cnt == 2:
                return False

        return True


sol = Solution()

print(sol.checkPossibility([4, 2, 3]))
print(sol.checkPossibility([4, 2, 1]))
print(sol.checkPossibility([3, 4, 2, 3]))

