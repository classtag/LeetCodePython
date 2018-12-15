# -*- coding: utf-8 -*-


class Solution:

  def searchInsert(self, A, target):
    """
    :type A list
    :type target int
    :rtype int
    """
    if not A:
      return 0

    start, end = 0, len(A) - 1
    while start + 1 < end:
      mid = start + (end - start) // 2
      if target == A[mid]:
        return mid
      elif target > A[mid]:
        start = mid
      else:
        end = mid

    if A[start] >= target:
      return start
    if A[end] >= target:
      return end
    return len(A)


if __name__ == '__main__':
  s = Solution()
  rs = s.searchInsert([1, 3, 5, 8], 7)
  print(rs)
