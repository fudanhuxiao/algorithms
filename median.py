from heapq import *
class MedianOfAStream:
  def __init__(self):
    self.maxheap = []
    self.minheap = []
  def insert_num(self, num):
    # TODO: Write your code here
    # make the maxheap same size or 1 more than minheap
    if len(self.maxheap) == len(self.minheap):
      if not self.minheap or num <= self.minheap[0]:
        heappush(self.maxheap, -num)
      else:
        n = heappop(self.minheap)
        heappush(self.minheap, num)
        heappush(self.maxheap, -n)
    else:
      if num < -self.maxheap[0]:
        n = -heappop(self.maxheap)
        heappush(self.maxheap, -num)
        heappush(self.minheap, n)
      else:
        heappush(self.minheap, num)

  def find_median(self):
    # TODO: Write your code here
    if len(self.maxheap) == len(self.minheap):
      return (-self.maxheap[0]+self.minheap[0])/2.0
    return -self.maxheap[0]
