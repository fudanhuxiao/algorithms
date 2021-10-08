from heapq import *
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        timebased = []
        for i in range(len(tasks)):
            timebased.append([tasks[i][0], tasks[i][1], i])
        timebased.sort()
        
        minheap = []
        heappush(minheap, [timebased[0][1], timebased[0][2]])
        t = timebased[0][0]
        i = 1
        ans = []
        while minheap:
            duration, idx = heappop(minheap)
            ans.append(idx)
            t += duration
            while i < len(timebased) and timebased[i][0] <= t:
                heappush(minheap, [timebased[i][1], timebased[i][2]])
                i += 1
            if not minheap and i < len(timebased):
                heappush(minheap, [timebased[i][1], timebased[i][2]])
                t = timebased[i][0]
                i += 1
        return ans
            
                    
            
