class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        t1, t2 = self.parse(s1), self.parse(s2)
        memo = {}
        return self.dfs(t1, 0, 0, t2, 0, 0, memo)
    
    def getNums(self, s):
        d = int(s)
        if len(s) == 1:
            return [d]
        elif len(s) == 2:
            return [d, d//10+d%10]
        else:
            a, b, c = d//100, d%100//10, d%10
            return [d, a+b+c, a+d%100, d//10+c]
    
    def dfs(self, t1, i1, num1, t2, i2, num2, memo):
        if (i1, num1, i2, num2) in memo:
            return memo[(i1, num1, i2, num2)]
        if i1 == len(t1) and i2 == len(t2):
            return num1 == num2
        if (i1 == len(t1) and num1 == 0) or (i2 == len(t2) and num2 == 0):
            return False
        if i1 < len(t1) and t1[i1][0].isdigit():
            for num in self.getNums(t1[i1]):
                if self.dfs(t1, i1+1, num1+num, t2, i2, num2, memo):
                    memo[(i1, num1, i2, num2)] = True
                    return True
            memo[(i1, num1, i2, num2)] = False
            return False
        elif i2 < len(t2) and t2[i2][0].isdigit():
            for num in self.getNums(t2[i2]):
                if self.dfs(t1, i1, num1, t2, i2+1, num2+num, memo):
                    memo[(i1, num1, i2, num2)] = True
                    return True
            memo[(i1, num1, i2, num2)] = False
            return False
        if num1 > 0 and num2 > 0:
            common = min(num1, num2)
            memo[(i1, num1, i2, num2)] = self.dfs(t1, i1, num1-common, t2, i2, num2-common, memo)
            return memo[(i1, num1, i2, num2)]
        elif num1 > 0:
            memo[(i1, num1, i2, num2)] = self.dfs(t1, i1, num1-1, t2, i2+1, num2, memo)
            return memo[(i1, num1, i2, num2)]
        elif num2 > 0:
            memo[(i1, num1, i2, num2)] = self.dfs(t1, i1+1, num1, t2, i2, num2-1, memo)
            return memo[(i1, num1, i2, num2)]
        else:
            if t1[i1] != t2[i2]:
                return False
            memo[(i1, num1, i2, num2)] = self.dfs(t1, i1+1, num1, t2, i2+1, num2, memo)
            return memo[(i1, num1, i2, num2)]
    
    def parse(self, s):
        t, i, n = [], 0, len(s)
        while i < n:
            if not s[i].isdigit():
                t.append(s[i])
                i += 1
            else:
                j = i+1
                while j < n and s[j].isdigit():
                    j += 1
                t.append(s[i:j])
                i = j
        return t
