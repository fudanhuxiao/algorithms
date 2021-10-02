class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(stickers)
        stkr = [[0]*26 for _ in range(n)]
        for i in range(n):
            for c in stickers[i]:
                stkr[i][ord(c)-ord('a')] += 1
        dp = {}
        dp[''] = 0
        def helper(target):
            if target in dp:
                return dp[target]
            tar = [0]*26
            for c in target:
                tar[ord(c)-ord('a')] += 1
            ans = float('inf')
            for i in range(len(stkr)):
                if stkr[i][ord(target[0])-ord('a')] == 0:
                    continue
                s = ''
                for j in range(26):
                    s += chr(ord('a')+j)*(tar[j]-min(tar[j], stkr[i][j]))
                temp = helper(s)
                ans = min(ans, temp+1)
            dp[target] = ans
            return dp[target] 
        helper(target)
        return dp[target] if dp[target] < float('inf') else -1
                
        
