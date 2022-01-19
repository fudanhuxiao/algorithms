class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        calc = lambda x: 1 if x == 1 else (2 if x <= 9 else (3 if x <= 99 else 4))
        n = len(s)
        dp = [[float('inf')]*(k+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(min(i, k)+1):
                if j > 0:
                    dp[i][j] = dp[i-1][j-1]
                same, diff = 0, 0
                for i0 in range(i, 0, -1):
                    if s[i0-1] == s[i-1]:
                        same += 1
                        dp[i][j] = min(dp[i][j], dp[i0-1][j-diff]+calc(same))
                    else:
                        diff += 1
                        if diff > j:
                            break
        return dp[n][k]
