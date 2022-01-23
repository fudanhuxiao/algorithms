class Greedy:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minheap = []
        n = len(nums)
        curmax = float('-inf')
        for i in range(n):
            heappush(minheap, (nums[i][0], i, 0))
            curmax = max(curmax, nums[i][0])
        high, low = float('inf'), float('-inf')
        while minheap:
            num, i, j = heappop(minheap)
            if curmax - num < high - low:
                    high, low = curmax, num
            if j+1 == len(nums[i]):
                break
            heappush(minheap, (nums[i][j+1], i, j+1))
            curmax = max(curmax, nums[i][j+1])
        return [low, high]
            
                
