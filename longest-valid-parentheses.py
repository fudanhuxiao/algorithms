class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, maxlen = 0, 0, 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, right+left)
            if right > left:
                right, left = 0, 0
        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, left+right)
            if left > right:
                left, right = 0, 0
        return maxlen
