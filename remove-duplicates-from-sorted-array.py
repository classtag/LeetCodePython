class Solution:

  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0:
      return 0

    index = 0
    for i in range(1, n):
      if nums[index] != nums[i]:
        index += 1
        nums[index] = nums[i]

    return index + 1
