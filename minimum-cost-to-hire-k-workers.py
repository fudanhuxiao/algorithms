class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = []
        for i in range(len(wage)):
            workers.append([wage[i]*1.0/quality[i], quality[i], wage[i]])
        workers.sort()
        qualitySum, ans, maxheap = 0, float('inf'), []
        for ratio, q, w in workers:
            heappush(maxheap, -q)
            qualitySum += q
            if len(maxheap) > k:
                qualitySum += heappop(maxheap)
            if len(maxheap) == k:
                ans = min(ans, ratio*qualitySum)
        return ans
