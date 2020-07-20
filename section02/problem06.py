class Solution:
    def validateStackSequences(self, pushed, popped):

        idx = 0
        tmp_list = []

        for i in pushed:
            tmp_list.append(i)
            while tmp_list and idx < len(popped) and tmp_list[-1] == popped[idx]:
                tmp_list.pop()
                idx += 1

        return idx == len(popped)


sol = Solution()
print(sol.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(sol.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
print(sol.validateStackSequences([2, 1, 0], [1, 2, 0]))

