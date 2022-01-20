class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def helper(arr):
            if len(arr) == 1:
                return abs(arr[0]-24) < 1e-6
            for i in range(len(arr)):
                for j in range(len(arr)):
                    if i != j:
                        n1, n2 = arr[i], arr[j]
                        newarr = []
                        for k in range(len(arr)):
                            if k != i and k != j:
                                newarr.append(arr[k])
                        for num in [n1+n2, n1*n2, n1-n2]:
                            newarr.append(num)
                            if helper(newarr):
                                return True
                            newarr.pop()
                        if n2 != 0:
                            newarr.append(n1/n2)
                            if helper(newarr):
                                return True
                            newarr.pop()
            return False
        return helper(cards)
