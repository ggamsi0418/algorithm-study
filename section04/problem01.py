"""
    [leetcode] 690. Employee Importance

    https://leetcode.com/problems/employee-importance/

"""
from collections import deque

# Definition for Employee.
class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def input_employee(input_list):
    result = []
    for e in input_list:
        e_id, e_importance, e_subordinates = e
        result.append(Employee(e_id, e_importance, e_subordinates))

    return result


class Solution:

    def dfs(self, team_chart, id):
        employee = team_chart[id]
        total = employee.importance
        check = deque(employee.subordinates)
        success = deque()
        while check:
            next_employee = check.popleft()
            if next_employee not in success:
                success.append(next_employee)
                total += team_chart[next_employee].importance
                if team_chart[next_employee].subordinates:
                    for i in team_chart[next_employee].subordinates:
                        check.append(i)

        return total


    def getImportance(self, employees, id):
        team_chart = {e.id : e for e in employees}
        return self.dfs(team_chart, id)


sol = Solution()
print(sol.getImportance(input_employee([[1,5,[2,3]],[2,3,[4]],[3,4,[]],[4,1,[]]]), 1))