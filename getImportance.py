"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapping = {}
        for i in range(len(employees)):
            mapping[employees[i].id] = i
        def helper(pid):
            employee = employees[mapping[pid]]
            ans = employee.importance
            if not employee.subordinates:
                return ans
            for i in employee.subordinates:
                ans += helper(i)
            return ans
        return helper(id)
            
