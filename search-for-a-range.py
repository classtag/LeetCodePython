# -*- coding: utf-8 -*-


class Solution:

  def searchRange(self, nums, target):
    """
    :type nums list
    :type target int
    :rtype list
    """
    n = len(nums)

    start, end = 0, n - 1
    while start + 1 < end:
      mid = start + (end - start) // 2
      if nums[mid] < target:
        start = mid
      else:
        end = mid

    if nums[start] == target:
      left_bound = start
    elif nums[end] == target:
      left_bound = end
    else:
      return [-1, 1]

    start, end = left_bound, n - 1
    while start + 1 < end:
      mid = start + (end - start) // 2
      if nums[mid] <= target:
        start = mid
      else:
        end = mid

    if nums[end] == target:
      right_bound = end
    else:
      right_bound = start

    return left_bound, right_bound


if __name__ == '__main__':
  s = Solution()
  rs = s.searchRange([1, 2, 3, 4, 4, 5, 6, 7, 8], 4)
  print(rs)
