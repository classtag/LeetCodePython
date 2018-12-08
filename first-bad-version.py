# -*- coding: utf-8 -*-

class SVNRepo:
    @classmethod
    def isBadVersion(cls, id):
        return id == 10


#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    def findFirstBadVersion(self, n):
        start, end = 0, n
        while start + 1 < end:
            mid = start + (end - start) // 2
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid
        if SVNRepo.isBadVersion(start):
            return start
        return end
