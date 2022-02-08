class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0]*n
        stack = []
        for i in range(n-1, -1, -1):
            n = 0
            while stack:
                n += 1
                if heights[i] >= stack[-1]:
                    stack.pop()
                else:
                    break
            ans[i] = n
            stack.append(heights[i])
        return ans
            
            
