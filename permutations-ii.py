# -*- coding: utf-8 -*-
# https://leetcode.com/problems/permutations-ii/
import copy


class Solution:

    def permuteUnique(self, nums):
        """
        :type nums list
        """
        nums = sorted(nums)
        results = []
        visited = [False for _ in nums]

        self.dfs(nums, visited, [], results)

        return results

    def dfs(self, nums, visited, permutation, results):
        """
        :type nums list
        :type visited list
        :type permutation list
        :type results list
        """
        if len(nums) == len(permutation):
            results.append(copy.copy(permutation))
            return

        for i, num in enumerate(nums):
            last_idx = i - 1
            duplicated = i > 0 and nums[last_idx] == num and not visited[last_idx]
            if visited[i] or duplicated:
                continue

            permutation.append(num)
            visited[i] = True
            self.dfs(nums, visited, permutation, results)
            visited[i] = False
            permutation.pop(len(permutation) - 1)


if __name__ == '__main__':
    s = Solution()
    permute_list = s.permuteUnique([1, 2, 2, 3])
    for permute in permute_list:
        print(permute)
