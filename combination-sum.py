# -*- coding: utf-8 -*-
# https://leetcode.com/problems/combination-sum/
import copy


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        result = []
        self.recurse(candidates, target, [], 0, result)
        return result

    def recurse(self, candidates, target, combination, pos, result):
        if target == 0:
            result.append(copy.copy(combination))
            return

        for i in range(pos, len(candidates)):
            candidate = candidates[i]
            new_target = target - candidate
            if new_target >= 0:
                new_combination = copy.copy(combination)
                new_combination.append(candidate)
                self.recurse(candidates, new_target, new_combination, i,
                             result)
            else:
                break


if __name__ == '__main__':
    s = Solution()
    combination_list = s.combinationSum([2, 3, 6, 7], 7)
    for rs in combination_list:
        print(rs)
