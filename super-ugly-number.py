class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0]*(n+1)
        m = len(primes)
        # point to the dp that each prime should multiply with
        pointers = [0]*m
        # current list of m numbers that each prime multiplied with their dp
        num = [1]*m
        
        for i in range(1, n+1):
            minnum = min(num)
            dp[i] = minnum
            for j in range(m):
                if num[j] == minnum:
                    pointers[j] += 1
                    num[j] = dp[pointers[j]]*primes[j]
        return dp[n]
