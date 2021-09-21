class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)-k+1
        dp = [0]*n
        presum = 0
        for i in range(len(nums)):
            presum += nums[i]
            if i >= k-1:
                dp[i-k+1] = presum
                presum -= nums[i-k+1]
        left = [0]*n
        right = [n-1]*n
        maxidx = 0
        for i in range(1, n):
            if dp[i] > dp[maxidx]:
                maxidx = i
            left[i] = maxidx
        maxidx = n-1
        for i in range(n-2, -1, -1):
            if dp[i] >= dp[maxidx]:
                maxidx = i
            right[i] = maxidx
        ans = [-1]*3
        for i in range(k, len(nums)-k-k+1):
            if ans[0] == -1 or dp[left[i-k]]+dp[i]+dp[right[i+k]] > dp[ans[0]]+dp[ans[1]]+dp[ans[2]]:
                ans = [left[i-k], i, right[i+k]]
        return ans
            
