# -*- coding: utf-8 -*-


class Solution:

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0

        class UnionFind(object):
            def __init__(self, n_groups):
                # 初始化 n_groups 个集合，然后每个集合的老大是数组的下标
                self.set = list(range(n_groups))
                self.count = n_groups

            def find_set(self, x):
                if self.set[x] != x:
                    self.set[x] = self.find_set(self.set[x])  # path compression.
                return self.set[x]

            def union_set(self, x, y):
                """合并两个集合"""
                # 找到各自的根节点
                x_root, y_root = map(self.find_set, (x, y))
                if x_root != y_root:  # 如果两个根节点也不在同一个集合中，那么就合并这两个集合
                    # 节点下标小的把根节点指向节点下表大的
                    self.set[min(x_root, y_root)] = max(x_root, y_root)
                    # 合并完成后，集合个数减少1
                    self.count -= 1

        rows = len(M)
        circles = UnionFind(rows)
        for i in range(rows):
            for j in range(rows):
                if M[i][j] == 1 and i != j:
                    circles.union_set(i, j)
        return circles.count
