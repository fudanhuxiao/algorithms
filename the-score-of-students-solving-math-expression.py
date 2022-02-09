class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        total, cur = 0, 1
        for i in range(len(s)):
            if s[i] != '*' and s[i] != '+':
                cur *= int(s[i])
            if s[i] == '+' or i == len(s)-1:
                total += cur
                cur = 1
        orders = self.compute(s, {})
        ret = 0
        for a in answers:
            if a == total:
                ret += 5
            elif a in orders:
                ret += 2
        return ret
        
    def compute(self, s, memo):
        if s.isdigit():
            return set([int(s)])
        if s in memo:
            return memo[s]
        memo[s] = set()
        for i in range(len(s)):
            if s[i] == '+' or s[i] == '*':
                left = self.compute(s[:i], memo)
                right = self.compute(s[i+1:], memo)
                for l in left:
                    for r in right:
                        if s[i] == '+' and l+r <= 1000:
                            memo[s].add(l+r)
                        elif s[i] == '*' and l*r <= 1000:
                            memo[s].add(l*r)
        return memo[s]
        
