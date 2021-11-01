class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if citations[0] >= n:
            return n
        start, end = 0, n-1
        ans = 0
        while start <= end:
            mid = (start+end)//2
            h = n-mid
            if citations[mid] >= h:
                if citations[mid-1] <= h:
                    ans = max(ans, h)
                end = mid-1
            else:
                start = mid+1
        return ans
                
                
