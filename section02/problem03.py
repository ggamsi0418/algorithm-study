"""
    621. Task Scheduler
    https://leetcode.com/problems/task-scheduler/

    참고: https://leetcode.com/problems/task-scheduler/discuss/104507/Python-Straightforward-with-Explanation
"""
import collections


class Solution:
    def leastInterval(self, tasks, n):
        tasks_count = list(collections.Counter(tasks).values())
        max_count = max(tasks_count)
        max_count_tasks = tasks_count.count(max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)


sol = Solution()
print(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0))
print(sol.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))

