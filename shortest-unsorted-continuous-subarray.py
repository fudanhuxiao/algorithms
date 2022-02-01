class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxnum, minnum = nums[0], nums[n-1]
        left, right = 0, -1
        for i in range(n):
            if nums[i] >= maxnum:
                maxnum = nums[i]
            else:
                right = i
            if nums[n-1-i] <= minnum:
                minnum = nums[n-1-i]
            else:
                left = n-1-i
        return right-left+1
