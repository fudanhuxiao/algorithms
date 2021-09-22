class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0]*121
        for age in ages:
            count[age] += 1
        prefix = [0]*121
        presum = 0
        for i in range(1, 121):
            presum += count[i]
            prefix[i] = presum
        ans = 0
        for age in range(1, 121):
            low = int(0.5*age+7)
            ans += max(prefix[age-1]-prefix[low], 0)*count[age]
            if count[age] > 1 and age > 0.5*age+7:
                ans += count[age]*(count[age]-1)
        return ans
            
            
