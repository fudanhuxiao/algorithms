class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        d = {}
        for i in range(len(nums)):
            m = nums[i]//(t+1)
            if m in d:
                return True
            if m-1 in d and abs(nums[i]-d[m-1]) <= t:
                return True
            if m+1 in d and abs(nums[i]-d[m+1]) <= t:
                return True
            d[m] = nums[i]
            if i >= k:
                del d[nums[i-k]//(t+1)]
        return False
