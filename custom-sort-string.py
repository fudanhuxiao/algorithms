class Solution:
    def customSortString(self, order: str, s: str) -> str:
        inorder = {}
        for c in order:
            inorder[c] = 0
        outorder = []
        for c in s:
            if c in inorder:
                inorder[c] += 1
            else:
                outorder.append(c)
        for c in order:
            outorder.extend([c]*inorder[c])
        return ''.join(outorder)
        
        
