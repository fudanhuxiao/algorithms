class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []
        for i in range(m+n-1):
            if i % 2 == 0:
                r = i if i < m else m-1
                c = 0 if i < m else i-(m-1)
                while r >= 0 and c < n:
                    ans.append(mat[r][c])
                    r -= 1
                    c += 1
            else:
                r = 0 if i < n else i-(n-1)
                c = i if i < n else n-1
                while r < m and c >= 0:
                    ans.append(mat[r][c])
                    r += 1
                    c -= 1
        return ans
            
            
