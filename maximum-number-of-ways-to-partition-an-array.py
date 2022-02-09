class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum = [0]*n
        presum[0] = nums[0]
        cntR = {}
        for i in range(1, n):
            presum[i] = presum[i-1]+nums[i]
            cntR[presum[i-1]] = cntR.get(presum[i-1],0)+1
        total = presum[n-1]
        ways = 0
        if total % 2 == 0:
            ways = cntR.get(total//2,0)
        cntL = {}
        for i in range(n):
            # 修改nums[i]为k，i左侧的presum不变，i及右侧presum+=d
            d = k-nums[i]
            if (total+d) % 2 == 0:
                ways = max(ways, cntL.get((total+d)//2,0)+cntR.get((total-d)//2,0))
            cntL[presum[i]] = cntL.get(presum[i],0)+1
            cntR[presum[i]] = cntR.get(presum[i],0)-1
        return ways
