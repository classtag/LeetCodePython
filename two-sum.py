# -*- coding: utf-8 -*-
# 1 https://leetcode.com/problems/two-sum/


class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = dict()

        for idx, num in enumerate(nums):
            diff_num = target - num
            diff_idx = hash_map.get(diff_num)
            if diff_idx is None:
                hash_map[num] = idx
            else:
                return [diff_idx, idx]

        return [-1, -1]
