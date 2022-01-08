class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3
        dp = [0]*(n+1)
        mode = 10**9+7
        dp[0], dp[1], dp[2] = 1, 2, 4
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
            dp[i] %= mode
        oneA = 0
        for i in range(n):
            oneA += dp[i]*dp[n-1-i]
            oneA %= mode
        return (dp[n]+oneA)%mode
