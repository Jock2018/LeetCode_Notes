#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/9/12 22:08
LeetCode原题链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
"""

# import functools
import functools
from typing import List


# class Solution:
#     """解法一：递归"""
#
#     def numWays(self, n: int) -> int:
#         if n == 0:
#             return 1
#         if n == 1:
#             return 1
#         return self.numWays(n - 1) + self.numWays(n - 2)


# class Solution:
#     """解法二：递归 + lru 缓存"""
#
#     @functools.lru_cache
#     def numWays(self, n: int) -> int:
#         if n == 0:
#             return 1
#         if n == 1:
#             return 1
#         return self.numWays(n - 1) + self.numWays(n - 2)


class Solution:
    """解法三：递归 + 缓存"""

    def numWays(self, n: int) -> int:
        memo = [-1] * (n + 1)
        return self._jump(n, memo)

    def _jump(self, n: int, memo: List[int]) -> int:
        if n in (0, 1):
            return 1
        if n == 2:
            return 2
        if memo[n] > -1:
            return memo[n]
        memo[n] = (self._jump(n - 1, memo) + self._jump(n - 2, memo)) % (10 ** 9 + 7)
        return memo[n]


# if __name__ == "__main__":
#     solution = Solution()
#     assert solution.numWays(2) == 2
#     assert solution.numWays(0) == 1
#     assert solution.numWays(7) == 21
