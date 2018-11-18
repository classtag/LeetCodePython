# -*- coding: utf-8 -*-
# https://leetcode.com/problems/house-robber-ii/description/


class Solution:

    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(self.rob_row(nums[1:]), self.rob_row(nums[:-1]))

    def rob_row(self, nums):
        cache = [0] * len(nums)
        cache[0], cache[1] = nums[0], max(nums[:2])

        for i in range(2, len(nums)):
            cache[i] = max(cache[i - 1], cache[i - 2] + nums[i])

        return cache[-1]
