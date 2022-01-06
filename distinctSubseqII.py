class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp, last = [1], {}
        for i in range(len(s)):
            dp.append(dp[-1]*2)
            if s[i] in last:
                dp[-1] -= dp[last[s[i]]]
            last[s[i]] = i
        return (dp[-1]-1)%(10**9+7)
