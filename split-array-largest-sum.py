class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def isValid(maxsum, m):
            parts, cursum = 1, 0
            for n in nums:
                if cursum+n > maxsum:
                    parts += 1
                    cursum = n
                else:
                    cursum += n
                if parts > m:
                    return False
            return True
                
        start, end = max(nums), sum(nums)
        while start < end:
            mid = (start+end)//2
            if isValid(mid, m):
                end = mid
            else:
                start = mid+1
        return start
        
