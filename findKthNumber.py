class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(x):
            count = 0
            for i in range(1, m+1):
                count += min(x//i, n)
            return count >= k
        
        start, end = 1, m*n
        while start + 1 < end:
            mid = (start+end)//2
            if enough(mid):
                end = mid
            else:
                start = mid + 1
        return start if enough(start) else end
