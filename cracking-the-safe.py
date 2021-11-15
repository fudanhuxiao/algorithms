class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # k^n ways of password, maxlen = n*k^n
        def dfs(curr, counted, total):
            if len(counted)==total:
                return curr
            
            for i in range(k):
                # last n-1 char+a random char
                tmp = curr[-(n-1):]+str(i) if n!=1 else str(i)
                if tmp not in counted:
                    counted.add(tmp)
                    res = dfs(curr+str(i), counted, total)
                    if res:
                        return res
                    counted.remove(tmp)
                    
        return dfs("0"*n, set(["0"*n]), k**n)
