class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        start, end = 0, nums[-1]-nums[0]
        while start + 1 < end:
            mid = (start+end)//2
            if self.countSmaller(nums, mid) >= k:
                end = mid
            else:
                start = mid+1
        return start if self.countSmaller(nums, start) >= k else end
    
    def countSmaller(self, nums, dist):
        count = 0
        left = 0
        for right in range(len(nums)):
            while nums[right]-nums[left] > dist:
                left += 1
            count += right-left
        return count
                
