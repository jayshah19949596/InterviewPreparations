"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, query_id):
        emap = {e.id: e for e in employees}

        def dfs(eid):
            employee = emap[eid]
            subord_imp = 0
            for eid in employee.subordinates:
                subord_imp += dfs(eid)

            return employee.importance + subord_imp

        return dfs(query_id)
