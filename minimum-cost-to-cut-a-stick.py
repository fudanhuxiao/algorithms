class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        m = len(cuts)
        dp = [[0]*m for _ in range(m)]
        for l in range(2, m):
            for i in range(m-l):
                j = i+l
                cur = float('inf')
                for k in range(i+1, j):
                    cur = min(cur, dp[i][k]+dp[k][j]+cuts[j]-cuts[i])
                dp[i][j] = cur if cur < float('inf') else 0
        return dp[0][m-1]
