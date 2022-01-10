class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        index = defaultdict(list)
        for i in range(n):
            index[s[i]].append(i)
        ans = 0
        for ls in index.values():
            ls = [-1] + ls + [n]
            for i in range(1, len(ls)-1):
                ans += (ls[i]-ls[i-1])*(ls[i+1]-ls[i])
        return ans
