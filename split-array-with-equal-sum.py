class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 7:
            return False
        preSum = [nums[0]]
        for i in range(1, n):
            preSum.append(preSum[i-1]+nums[i])
        
        for j in range(3, n-3):
            subSum = set()
            for i in range(1, j-1):
                if preSum[i-1] == preSum[j-1]-preSum[i]:
                    subSum.add(preSum[i-1])
            for k in range(j+2, n-1):
                if preSum[k-1]-preSum[j] == preSum[n-1]-preSum[k] and (preSum[n-1]-preSum[k]) in subSum:
                    return True
        return False
