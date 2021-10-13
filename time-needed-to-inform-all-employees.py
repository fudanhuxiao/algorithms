class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)
        self.maxtime = 0
        def helper(idx, time):
            if idx not in graph:
                self.maxtime = max(self.maxtime, time)
            for child in graph[idx]:
                helper(child, time+informTime[idx])
        helper(headID, 0)
        return self.maxtime
        
            
