class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        boundaries = []
        for left, right, _ in buildings:
            boundaries.append(left)
            boundaries.append(right)
        boundaries.sort()
        i = 0
        maxheap = []
        ans = []
        for boundary in boundaries:
            while i < len(buildings) and buildings[i][0] <= boundary:
                heappush(maxheap, (-buildings[i][2], buildings[i][1]))
                i += 1
            while maxheap and maxheap[0][1] <= boundary:
                heappop(maxheap)
            maxn = 0 if not maxheap else -maxheap[0][0]
            if not ans or maxn != ans[-1][1]:
                ans.append([boundary, maxn])
        return ans
