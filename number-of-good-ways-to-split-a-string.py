class Solution:
    def numSplits(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0)+1
        ans = 0
        left = set()
        for c in s:
            left.add(c)
            freq[c] -= 1
            if freq[c] == 0:
                del freq[c]
            if len(left) == len(freq):
                ans += 1
        return ans
