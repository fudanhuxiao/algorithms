class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = float('-inf')
        stack = deque([(points[0][0], -points[0][0]+points[0][1])])
        for i in range(1, len(points)):
            while stack and points[i][0]-stack[0][0] > k:
                stack.popleft()
            if stack:
                ans = max(ans, points[i][0]+points[i][1]+stack[0][1])
            temp = -points[i][0]+points[i][1]
            while stack and stack[-1][1] < temp:
                stack.pop()
            stack.append((points[i][0], temp))
        return ans
