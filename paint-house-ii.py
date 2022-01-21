class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        m, n = len(costs), len(costs[0])
        if m <= 0 or n <= 0:
            return 0
        j1, low1, low2 = -1, float('inf'), float('inf')
        for j in range(n):
            if costs[0][j] < low1:
                j1 = j
                low2 = low1
                low1 = costs[0][j]
            elif costs[0][j] < low2:
                low2 = costs[0][j]
        
        for i in range(1, m):
            curj1, curlow1, curlow2 = -1, float('inf'), float('inf')
            for j in range(n):
                if j1 == j:
                    dp = low2 + costs[i][j]
                else:
                    dp = low1 + costs[i][j]
                if dp < curlow1:
                    curlow2 = curlow1
                    curj1 = j
                    curlow1 = dp
                elif dp < curlow2:
                    curlow2 = dp
            j1, low1, low2 = curj1, curlow1, curlow2
        return low1
        
