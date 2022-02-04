class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        ans = float('inf')
        pset = {(x, y) for x,y in points}
        for i in range(n-2):
            x1, y1 = points[i]
            for j in range(i+1, n-1):
                x2, y2 = points[j]
                for k in range(j+1, n):
                    x3, y3 = points[k]
                    if (x2-x1)*(x3-x1) + (y2-y1)*(y3-y1) == 0 and (x2+x3-x1, y2+y3-y1) in pset:
                        area = (((x1-x3)**2+(y1-y3)**2)*((x1-x2)**2+(y1-y2)**2))**0.5
                        ans = min(ans, area)
        return ans if ans < float('inf') else 0
                        
