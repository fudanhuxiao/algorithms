class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        ans = [['.']*m for i in range(n)]
        for i in range(m):
            base = n-1
            for j in range(n-1, -1, -1):
                if box[i][j] == '#':
                    ans[base][m-i-1] = '#'
                    base -= 1
                elif box[i][j] == '*':
                    ans[j][m-i-1] = '*'
                    base = j-1
        return ans
                    
