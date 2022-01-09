class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[1]*n for _ in range(n)]
        for l in range(1, n):
            for i in range(n-l):
                j = i+l
                dp[i][j] = l+1
                for k in range(i, j):
                    total = dp[i][k] + dp[k+1][j]
                    if s[k] == s[j]:
                        total -= 1
                    dp[i][j] = min(dp[i][j], total)
        return dp[0][n-1]
            
