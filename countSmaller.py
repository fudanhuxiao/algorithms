class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [[nums[i], i] for i in range(n)]
        ans = [0]*n
        
        def merge_sort(left, right):
            if left >= right:
                return
            mid = (left+right)//2
            merge_sort(left, mid)
            merge_sort(mid+1, right)
            merge(left, right)
            
        def merge(left, right):
            mid = (left+right)//2
            i, j = left, mid+1
            temp = []
            while i <= mid and j <= right:
                if arr[i][0] > arr[j][0]:
                    temp.append(arr[j])
                    j += 1
                else:
                    ans[arr[i][1]] += j-mid-1
                    temp.append(arr[i])
                    i += 1
            while i <= mid:
                ans[arr[i][1]] += j-mid-1
                temp.append(arr[i])
                i += 1
            while j <= right:
                temp.append(arr[j])
                j += 1
            for i in range(left, right+1):
                arr[i] = temp[i-left]
        
        merge_sort(0, n-1)
        return ans
        
