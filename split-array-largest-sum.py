# -*- coding: utf-8 -*-
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        N = len(nums)
        if N == m:
            return max(nums)

        L, R = max(nums), sum(nums) + 1
        ans = 0
        while L < R:
            mid = (L + R) // 2
            if self.guess(mid, nums, m):
                ans = mid
                R = mid
            else:
                L = mid + 1
        return ans

    @staticmethod
    def guess(mid, nums, m):
        sum = 0
        for i in range(0, len(nums)):
            if sum + nums[i] > mid:
                m -= 1
                sum = nums[i]
                if nums[i] > mid:
                    return False
            else:
                sum += nums[i]
        return m >= 1
