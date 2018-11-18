

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_set = set(nums)
        res = 0
        while hash_set:
            elem = hash_set.pop()
            high, low  = elem, elem
            while low - 1 in hash_set:
                hash_set.remove(low-1)
                low -= 1
                
            while high + 1 in hash_set:
                hash_set.remove(high+1)
                high += 1
            res = max(high-low+1,res)
        return res