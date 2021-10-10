class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k+maxPts <= n:
            return 1
        dp = [0]*(k+maxPts)
        for i in range(k, n+1):
            dp[i] = 1
        temp = n-k+1
        for i in range(k-1, -1, -1):
            dp[i] = temp/float(maxPts)
            temp = temp + dp[i] - dp[i+maxPts]
        return dp[0]
