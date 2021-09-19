class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k1 = len(mat1), len(mat1[0])
        k2, n = len(mat2), len(mat2[0])
        if k1 != k2:
            return None
        ans = [[None]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                num = 0
                for k in range(k1):
                    num += mat1[i][k]*mat2[k][j]
                ans[i][j] = num
        return ans
