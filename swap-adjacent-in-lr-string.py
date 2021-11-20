class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        a = [[start[i], i] for i in range(n) if start[i] == 'L' or start[i] == 'R']
        b = [[end[i], i] for i in range(n) if end[i] == 'L' or end[i] == 'R']
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            s, si = a[i]
            e, ei = b[i]
            if s != e:
                return False
            if (s == 'L' and si < ei) or (s == 'R' and si > ei):
                    return False
        return True
