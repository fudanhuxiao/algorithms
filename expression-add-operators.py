class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        num = list(num)
        exp = [None]*len(num)*2
        
        def dfs(pos, elen, prev, val):
            if pos >= len(num):
                if val == target:
                    ans.append(''.join(exp[:elen]))
                return
            n = 0
            prev_elen = elen
            if pos != 0:
                elen += 1
            for l in range(1, len(num)-pos+1):
                if num[pos] == '0' and l > 1:
                    break
                n = n*10+ord(num[pos+l-1])-ord('0')
                exp[elen] = num[pos+l-1]
                elen += 1
                if pos == 0:
                    dfs(l, elen, n, n)
                else:
                    exp[prev_elen] = '+'
                    dfs(pos+l, elen, n, val+n)
                    exp[prev_elen] = '-'
                    dfs(pos+l, elen, -n, val-n)
                    exp[prev_elen] = '*'
                    dfs(pos+l, elen, prev*n, val-prev+prev*n)
        
        dfs(0, 0, 0, 0)
        return ans
