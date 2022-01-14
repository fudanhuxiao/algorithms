class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1]*n
        maxlen, idx = 0, -1
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
            if dp[i] > maxlen:
                maxlen = dp[i]
                idx = i
        ans = [nums[idx]]
        idx -= 1
        maxlen -= 1
        while maxlen > 0:
            if dp[idx] == maxlen and ans[-1] % nums[idx] == 0:
                ans.append(nums[idx])
                maxlen -= 1
            idx -= 1
        return ans
