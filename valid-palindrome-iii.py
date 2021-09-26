class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        memo = [0]*n
        for i in range(n-2, -1, -1):
            # prev is memo[i+1][j-1]
            prev = 0
            for j in range(i+1, n):
                temp = memo[j]
                if s[i] == s[j]:
                    memo[j] = prev
                else:
                    memo[j] = 1 + min(memo[j-1], memo[j])
                prev = temp
        return memo[n-1] <= k
                    
