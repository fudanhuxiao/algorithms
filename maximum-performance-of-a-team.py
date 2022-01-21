class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = []
        for i in range(n):
            engineers.append((efficiency[i], speed[i]))
        engineers.sort(reverse=True)
        ans, total, minheap = 0, 0, []
        for e, s in engineers:
            total += s
            ans = max(ans, total*e)
            heappush(minheap, s)
            if len(minheap) >= k:
                total -= heappop(minheap)
        return ans%(10**9+7)
