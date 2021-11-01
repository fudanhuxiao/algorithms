class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def helper(cur, k, n, ans, start):
            if len(cur) == k and n == 0:
                ans.append(list(cur))
            if len(cur) >= k or n <= 0:
                return
            for num in range(start, 10):
                cur.append(num)
                helper(cur, k, n-num, ans, num+1)
                cur.pop()
        helper([], k, n, ans, 1)
        return ans
