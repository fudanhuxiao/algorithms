class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        dupe = sorted(arr)
        sub, ans = 0, 0
        for i in range(len(arr)):
            sub += arr[i]-dupe[i]
            if sub == 0:
                ans += 1
        return ans
