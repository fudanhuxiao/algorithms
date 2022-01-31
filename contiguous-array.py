class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        presum = {0:-1}
        total = 0
        ans = 0
        for i in range(n):
            if nums[i] == 1:
                total += 1
            else:
                total -= 1
            if total in presum:
                ans = max(ans, i-presum[total])
            else:
                presum[total] = i
        return ans
        
