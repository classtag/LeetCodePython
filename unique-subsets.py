# -*- coding: utf-8 -*-
# https://www.lintcode.com/problem/unique-subsets/


class Solution:

    def uniqueSubsets(self, nums):
        nums = sorted(nums)
        self.helper([], nums, 0)

    def helper(self, path, nums, pos):
        print(path)

        for i in range(pos, len(nums)):
            if i > 0 and i != pos and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.helper(path, nums, i + 1)
            path.pop(-1)


if __name__ == '__main__':
    s = Solution()
    s.uniqueSubsets([1, 2, 2])
