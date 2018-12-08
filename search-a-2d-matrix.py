# -*- coding: utf-8 -*-

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        """
        :type matrix list
        :type target int
        :rtype bool
        """
        if not matrix:
            return False

        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, rows * cols - 1

        while start + 1 < end:
            mid = int((start + end) / 2)
            x, y = int(mid / cols), int(mid % cols)  # return the row index and col index of mid
            num = matrix[x][y]
            if num == target:
                return True
            elif num < target:
                start = mid + 1
            else:
                end = mid - 1

        return False


if __name__ == '__main__':
    s = Solution()
    s.searchMatrix()
