class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x0, y0 = location
        extra, ls = 0, []
        for x, y in points:
            if x == x0 and y == y0:
                extra += 1
            else:
                ls.append((math.atan2(y - y0, x - x0)* (180 / math.pi) + 360) % 360)
        ls = ls + [a + 360 for a in ls]
        ls.sort()
        left, ans = 0, 0
        for right in range(len(ls)):
            while ls[right] - ls[left] > angle:
                left += 1
            ans = max(ans, right-left+1)
        return ans+extra
            
            
