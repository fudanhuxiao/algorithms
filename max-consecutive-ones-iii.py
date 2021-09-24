class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        slow, fast = 0, 0
        preSum = 0
        ans = 0
        for fast in range(len(nums)):
            preSum += 1 if nums[fast] == 0 else 0
            if preSum > k:
                while slow < fast and nums[slow] == 1:
                    slow += 1
                slow += 1
                preSum -= 1
            ans = max(ans, fast-slow+1)
        return ans
