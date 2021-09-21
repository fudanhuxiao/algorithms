class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def missing(idx):
            return nums[idx]-nums[0]-idx
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = start+(end-start)//2
            if missing(mid) < k:
                start = mid
            else:
                end = mid
        return nums[end]+k-missing(end) if missing(end) < k else nums[start]+k-missing(start)
