# -*- coding: utf-8 -*-
# https://leetcode.com/problems/kth-largest-element-in-a-stream
import heapq

# https://docs.python.org/3.0/library/heapq.html


class KthLargest:

  def __init__(self, k, nums):
    """
        :type k: int
        :type nums: List[int]
        """
    self.pool = nums
    self.k = k
    heapq.heapify(self.pool)
    while len(self.pool) > k:
      heapq.heappop(self.pool)

  def add(self, val):
    """
        :type val: int
        :rtype: int
        """
    if len(self.pool) < self.k:
      heapq.heappush(self.pool, val)
    elif val > self.pool[0]:
      heapq.heapreplace(self.pool, val)
      # heappushpop 是先压入，在弹出，压入候有一个排序调整过程
      # 而heapreplace是先弹出最小的，然后压入，不存在对堆的扩容过程
    return self.pool[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
