class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for x, y in points:
            slopes = {}
            maxfreq = 0
            for i, j in points:
                if x == i and y == j:
                    continue
                if j==y:
                    slope = '#'
                else:
                    slope = (i-x)/(j-y)
                slopes[slope] = slopes.get(slope, 0)+1
                maxfreq = max(maxfreq, slopes[slope])
            ans = max(ans, maxfreq+1)
        return ans
            
