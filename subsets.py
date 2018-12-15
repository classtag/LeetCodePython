# -*- coding: utf-8 -*-
# https://www.lintcode.com/problem/subsets/description


class Solution:

  def subsets(self, nums):
    nums = sorted(nums)
    path = list()

    self.helper(path, nums, 0)

  def helper(self, path, nums, pos):
    """
    Parameters
    ----------
    path: list of the access paths
    nums: the ordered nums list
    pos: the current access pos

    :type path list
    :type nums list
    :type pos int
    """
    print(path)
    for i in range(pos, len(nums)):
      path.append(nums[i])
      self.helper(path, nums, i + 1)
      path.pop(len(path) - 1)


if __name__ == '__main__':
  s = Solution()
  s.subsets([1, 2, 3])
