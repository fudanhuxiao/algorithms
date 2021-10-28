class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = [0]
        for i in range(n):
            preSum.append(preSum[-1]+nums[i])
        queue = deque()
        ans = n+1
        for i in range(n+1):
            while queue and preSum[queue[-1]] >= preSum[i]:
                queue.pop()
            while queue and preSum[i] - preSum[queue[0]] >= k:
                ans = min(ans, i-queue.popleft())
            queue.append(i)
        return ans if ans < n+1 else -1
                
                
            
