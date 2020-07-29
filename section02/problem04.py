from collections import deque


class Solution:
    def sumSubarrayMins(self, A):
        length = len(A)
        answer = deque()

        for i in range(1, length + 1):
            for j in range(0, length):
                if j >= i:
                    break
                answer.append(min(A[j:i]))
            print(answer)
        return sum(answer)


sol = Solution()
print(sol.sumSubarrayMins([71, 55, 82, 55]))
