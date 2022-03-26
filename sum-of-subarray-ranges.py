class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        def getCount(isMin):
            stack = []
            ans = []
            for i in range(n):
                while stack and ((isMin and nums[stack[-1]] >= nums[i]) or (not isMin and nums[stack[-1]] <= nums[i])):
                    stack.pop()
                left = -1 if not stack else stack[-1]
                ans.append(left)
                stack.append(i)
            stack = []
            for j in range(n-1, -1, -1):
                while stack and ((isMin and nums[stack[-1]] > nums[j]) or (not isMin and nums[stack[-1]] < nums[j])):
                    stack.pop()
                right = n if not stack else stack[-1]
                ans[j] = (j-ans[j])*(right-j)
                stack.append(j)
            return ans
            
        mincount = getCount(True)
        maxcount = getCount(False)
        ans = 0
        for i in range(n):
            ans += (maxcount[i]-mincount[i])*nums[i]
        return ans
