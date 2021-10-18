from heapq import *
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minheap = []
        for s in sticks:
            heappush(minheap, s)
        cost = 0
        while len(minheap) > 1:
            l,r =  heappop(minheap), heappop(minheap)
            cost += l+r
            heappush(minheap, l+r)
        return cost
        
