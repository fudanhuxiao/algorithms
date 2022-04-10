class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        n = len(nums)
        minnum = float('inf')
        maxheap = []
        for i in range(n):
            val = nums[i]
            if val % 2 == 1:
                val *= 2
            minnum = min(minnum, val)
            heappush(maxheap, -val)
        ans = float('inf')
        while maxheap and -maxheap[0] % 2 == 0:
            val = -heappop(maxheap)
            ans = min(ans, val-minnum)
            val //= 2
            minnum = min(minnum, val)
            heappush(maxheap, -val)
        ans = min(ans, -maxheap[0]-minnum)
        return ans
        
