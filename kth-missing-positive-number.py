class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k < arr[0]:
            return k
        if k > arr[-1] - n:
            return k+n
        start, end = 0, n-1
        while start < end:
            mid = (start+end)//2
            if k > arr[mid]-mid-1:
                start = mid+1
            else:
                end = mid
        return k+start
