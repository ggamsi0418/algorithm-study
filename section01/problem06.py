"""
1365. How Many Numbers Are Smaller Than the Current Number

(https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)
"""


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        checked_nums = {}
        answer = []

        for index, num in enumerate(nums):

            if num in checked_nums:
                answer.append(checked_nums[num])
                continue

            cnt = 0
            for i, v in enumerate(nums):
                if i == index:
                    continue
                if v < num:
                    cnt += 1

            answer.append(cnt)

        return answer


sol = Solution()
print(sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
print(sol.smallerNumbersThanCurrent([6, 5, 4, 8]))
print(sol.smallerNumbersThanCurrent([7, 7, 7, 7]))

