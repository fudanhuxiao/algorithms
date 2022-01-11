class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxnum, ans = 0, 0
        for i in range(len(arr)):
            maxnum = max(maxnum, arr[i])
            if maxnum == i:
                ans += 1
        return ans
