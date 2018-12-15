# -*- coding: utf-8 -*-
# DP
# https://leetcode.com/problems/house-robber/


class Solution:
    def __init__(self):
        self.memo = {}

    def search(self, idx, nums):
        """
        :type idx: int
        :type nums: list[int]
        :rtype: int
        """
        if idx < 0:
            return 0
        if idx in self.memo:
            return self.memo.get(idx)

        self.memo[idx] = max(nums[idx] + self.search(idx - 2, nums),
                             self.search(idx - 1, nums))
        return self.memo[idx]

    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.search(len(nums) - 1, nums)

    def rob2(self, nums):
        """
        f(0) = nums[0]
        f(1) = max(num[0], num[1])
        f(k) = max( f(k-2) + nums[k], f(k-1) )
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]

        cache = [0] * size
        cache[0], cache[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            cache[i] = max(cache[i - 2] + nums[i], cache[i - 1])

        return cache[-1]

    def rob3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0

        for num in nums:
            last, now = now, max(last + num, now)

        return now

    def rob4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # state
        dp = [0] * 2
        # init
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            # function
            dp[i % 2] = max(dp[(i - 1) % 2], dp[(i - 2) % 2] + nums[i])
        # answer
        return dp[(n - 1) % 2]
