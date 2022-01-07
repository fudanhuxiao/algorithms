class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        i, j = 0, 0
        start, minlen = -1, len(s1)+1
        while i < len(s1):
            if s1[i] == s2[j]:
                j += 1
            i += 1
            if j == len(s2):
                end = i
                j -= 1
                i -= 1
                while j >= 0:
                    if s1[i] == s2[j]:
                        j -= 1
                    i -= 1
                i += 1
                if end-i < minlen:
                    start, minlen = i, end-i
                i += 1
                j = 0
        return s1[start:start+minlen] if start != -1 else ""
                
    def dp(self, s1: str, s2: str) -> str:
        s1, s2 = '#'+s1, '#'+s2
        m, n = len(s1), len(s2)
        dp = [[0]*(n) for _ in range(m)]
        for i in range(m):
            dp[i][0] = i+1
        for i in range(1, m):
            for j in range(1, n):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        start, minlen = -1, m+1
        for i in range(1, m):
            if dp[i][n-1] != 0:
                if i-dp[i][n-1]+1 < minlen:
                    start, minlen = dp[i][n-1], i-dp[i][n-1]+1
        return s1[start:start+minlen] if minlen < m+1 else ""
