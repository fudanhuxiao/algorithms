from heapq import *
def find_Kth_smallest_number_maxheap(nums, k):
      # TODO: Write your code here
      maxheap = []
      for i in range(k):
            heappush(maxheap, -nums[i])
      for i in range(k, len(nums)):
            if nums[i] < -maxheap[0]:
                  heappop(maxheap)
                  heappush(maxheap, -nums[i])
      return -maxheap[0]
