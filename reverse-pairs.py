class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp = [0]*len(nums)
        return self.merge_sort(nums, 0, len(nums)-1, temp)
    
    def merge_sort(self, nums, start, end, temp):
        if start >= end:
            return 0
        mid = (start+end)//2
        n1 = self.merge_sort(nums, start, mid, temp)
        n2 = self.merge_sort(nums, mid+1, end, temp)
        ans = n1+n2
        j = mid+1
        for i in range(start, mid+1):
            while j <= end and nums[i] > 2*nums[j]:
                j += 1
            ans += j-mid-1
        self.merge(nums, start, end, temp)
        return ans      
        
    def merge(self, nums, start, end, temp):
        mid = (start+end)//2
        left_index, right_index = start, mid+1
        index = start
        while left_index <= mid and right_index <= end:
            if nums[left_index] < nums[right_index]:
                temp[index] = nums[left_index]
                left_index += 1
            else:
                temp[index] = nums[right_index]
                right_index += 1
            index += 1
        while left_index <= mid:
            temp[index] = nums[left_index]
            left_index += 1
            index += 1
        while right_index <= end:
            temp[index] = nums[right_index]
            right_index += 1
            index += 1
        for i in range(start, end+1):
            nums[i] = temp[i]
