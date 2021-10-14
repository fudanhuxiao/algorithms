class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[0]*4 for _ in range(n+2)]
        ans = 0
        for i in range(m):
            old = 0
            for j in range(n):
                if mat[i][j] == 1:
                    dp[j+1][0] = dp[j][0]+1
                    dp[j+1][1] = dp[j+1][1]+1
                    prev = dp[j+1][2]
                    dp[j+1][2] = old+1
                    old = prev
                    dp[j+1][3] = dp[j+2][3]+1
                    ans = max(ans, max(dp[j+1]))
                else:
                    old = dp[j+1][2]
                    dp[j+1] = [0,0,0,0]
        return ans
