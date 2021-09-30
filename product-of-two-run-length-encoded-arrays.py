class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(encoded1) and j < len(encoded2):
            v1, f1 = encoded1[i]
            v2, f2 = encoded2[j]
            p = v1*v2
            f = min(f1, f2)
            if f < f1:
                encoded1[i][1] -= f
            else:
                i += 1
            if f < f2:
                encoded2[j][1] -= f
            else:
                j += 1
            if not ans or ans[-1][0] != p:
                ans.append([p, f])
            else:
                ans[-1][1] += f
        return ans
