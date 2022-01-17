class Solution:
    def numTilings(self, n: int) -> int:
        dp = [[0]*2 for _ in range(n+1)]
        mode = 10**9+7
        dp[0][0], dp[1][0] = 1, 1
        for i in range(2, n+1):
            dp[i][0] = (dp[i-1][0]+dp[i-2][0]+2*dp[i-1][1])%mode
            dp[i][1] = (dp[i-2][0]+dp[i-1][1])%mode
        return dp[n][0]%mode
