class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxheap = []
        ans, prevLocation, tank = 0, 0, startFuel
        stations.append([target, 0])
        for location, capacity in stations:
            tank -= location-prevLocation
            while maxheap and tank < 0:
                tank -= heappop(maxheap)
                ans += 1
            if tank < 0:
                return -1
            prevLocation = location
            heappush(maxheap, -capacity)
        return ans
        
            
        
