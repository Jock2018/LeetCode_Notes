#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/9/12 21:35
LeetCode原题链接：https://leetcode-cn.com/problems/climbing-stairs/submissions/
"""

# import functools
from typing import List


# class Solution:
#     """解法一：递归"""
#
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return n
#         if n == 2:
#             return n
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# class Solution:
#     """解法二：递归 + lru 缓存"""
#
#     @functools.lru_cache
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return n
#         if n == 2:
#             return n
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution:
    """解法三：递归 + 缓存"""

    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        return self._climb(n, memo)

    def _climb(self, n: int, memo: List[int]) -> int:
        if n == 1:
            return n
        if n == 2:
            return n
        if memo[n] > 0:
            return memo[n]
        memo[n] = self._climb(n - 1, memo) + self._climb(n - 2, memo)
        return memo[n]

#
# if __name__ == "__main__":
#     solution = Solution()
#     assert solution.climbStairs(2) == 2
#     assert solution.climbStairs(3) == 3
