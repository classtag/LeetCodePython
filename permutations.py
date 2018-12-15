# -*- coding: utf-8 -*-
import copy


class Solution:

  def permutations(self, nums):
    nums = sorted(nums)
    results = []
    visited = [False for _ in range(len(nums))]
    self.dfs(nums, visited, [], results)
    return results

  def dfs(self, nums, visited, permutation, results):
    if len(nums) == len(permutation):
      results.append(copy.copy(permutation))
      return
    for i in range(len(nums)):
      if visited[i]:
        continue
      permutation.append(nums[i])
      visited[i] = True
      self.dfs(nums, visited, permutation, results)
      visited[i] = False
      permutation.pop(len(permutation) - 1)


if __name__ == '__main__':
  s = Solution()
  result_list = s.permutations([1, 2, 3])
  for rs in result_list:
    print(rs)
