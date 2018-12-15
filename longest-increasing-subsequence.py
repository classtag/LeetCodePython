# -*- coding: utf-8 -*-
import sys


class Solution(object):

  def longestIncreasingSubsequence(self, nums):
    if not nums:
      return 0

    dp = [1] * len(nums)

    for curr, val in enumerate(nums):
      for prev in range(curr):
        if nums[prev] < val:
          dp[curr] = max(dp[curr], dp[prev] + 1)

    return max(dp)

  def longestIncreasingSubsequence2(self, nums):
    if not nums:
      return 0

    min_last = [0] * len(nums)
    min_last[0] = sys.maxsize

    for i in range(len(nums)):
      index = self.binarySearch(min_last, nums[i])
      min_last[index] = nums[i]

    for i in range(len(nums), 0, -1):
      if min_last[i] != sys.maxsize:
        return i

    return 0

  def binarySearch(self, nums, target):
    start, end = 0, len(nums) - 1
    while start + 1 < end:
      mid = start + (end - start) / 2
      if nums[mid] < target:
        start = mid
      else:
        end = mid

    return end
