class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n-1
        while i-1 >= 0 and arr[i-1] <= arr[i]:
            i -= 1
        maxj = i
        i -= 1
        if i < 0:
            return arr
        j = i+1
        while j < n and arr[j] < arr[i]:
            if arr[j] > arr[maxj]:
                maxj = j
            j += 1
        arr[i], arr[maxj] = arr[maxj], arr[i]
        return arr
