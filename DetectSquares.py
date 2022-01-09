class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        if x not in self.points:
            self.points[x] = {}
        self.points[x][y] = self.points[x].get(y, 0)+1

    def count(self, point: List[int]) -> int:
        i, j = point
        ans = 0
        if i not in self.points:
            return 0
        for x in self.points:
            if x == i or j not in self.points[x]:
                continue
            d = abs(i-x)
            if j+d in self.points[x] and j+d in self.points[i]:
                ans += self.points[x][j+d]*self.points[x][j]*self.points[i][j+d]
            if j-d in self.points[x] and j-d in self.points[i]:
                ans += self.points[x][j-d]*self.points[x][j]*self.points[i][j-d]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
