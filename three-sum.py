# -*- coding: utf-8 -*-

# 15 https://leetcode.com/problems/3sum/description/


class Solution:

  def threeSum1(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
      return []

    nums.sort()
    res = set()

    # [-4,-1,-1, 0, 1, 2]
    for i, a in enumerate(nums[:-2]):
      if i >= 1 and nums[i] == nums[i - 1]:
        continue
      # 用一个set存放c = 0 - a - b
      c_set = set()
      for b in nums[i + 1:]:
        c = -a - b
        if b not in c_set:
          c_set.add(c)
        else:
          res.add((a, b, c))
    return map(list, res)

  def threeSum2(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
      return []
    nums.sort() # n*log(n) quick_sort
    ans = list()
    for i in range(len(nums) - 2):
      # remove the last computed value to avoid the duplicated value
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      low, high = i + 1, len(nums) - 1
      while low < high:
        s = nums[i] + nums[low] + nums[high]
        if s < 0:
          low += 1
        elif s > 0:
          high -= 1
        else:
          ans.append([nums[i], nums[low], nums[high]])
          # remove the duplicated value from low to high
          while low < high and nums[low] == nums[low + 1]:
            low += 1
          # remove the duplicated value from high to low
          while low < high and nums[high] == nums[high - 1]:
            high -= 1
          # move to center
          low += 1
          high -= 1
    return ans
