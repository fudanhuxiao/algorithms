import random
def find_Kth_smallest_number(nums, k):
      # TODO: Write your code here
      # use randomized partitioning quick sort
      return find_Kth_smallest_number_recursive(nums, k, 0, len(nums)-1)

def find_Kth_smallest_number_recursive(nums, k, start, end):
      p = partition(nums, k, start, end)
      if p == k-1:
            return nums[p]
      if p < k-1:
            return find_Kth_smallest_number_recursive(nums, k, p+1, end)
      if p > k-1:
            return find_Kth_smallest_number_recursive(nums, k, start, p-1)

def partition(nums, k, start, end):
      if start == end:
            return start
      randomIndex = random.randint(start, end)
      nums[end], nums[randomIndex] = nums[randomIndex], nums[end]
      pivot = nums[end]
      for i in range(start, end):
            if nums[i] < pivot:
                  nums[i], nums[start] = nums[start], nums[i]
                  start += 1
      nums[start], nums[end] = nums[end], nums[start]
      return start
