class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        for n in arr:
            if n-difference in d:
                d[n] = 1 + d[n-difference]
            else:
                d[n] = 1
        return max(d.values())
