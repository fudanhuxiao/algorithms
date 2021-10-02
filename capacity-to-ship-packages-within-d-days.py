class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:  
        def countDays(weights, capacity):
            count = 0
            i = 0
            while i < len(weights):
                weight = 0
                while i < len(weights) and weight+weights[i] <= capacity:
                    weight += weights[i]
                    i += 1
                count += 1
            return count
        start, end = max(weights), sum(weights)
        while start + 1 < end:
            mid = (start+end)//2
            if countDays(weights, mid) <= days:
                end = mid
            else:
                start = mid+1
        return start if countDays(weights, start) <= days else end
            
