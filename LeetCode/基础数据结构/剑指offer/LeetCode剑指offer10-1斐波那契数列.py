#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/9/12 22:43
LeetCode原题链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
"""
import functools
from typing import List


# class Solution:
#     """解法一：递归"""
#
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         return (self.fib(n - 1) + self.fib(n - 2)) % (10 ** 9 + 7)


# class Solution:
#     """解法二：递归 + lru缓存"""
#
#     @functools.lru_cache
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         return (self.fib(n - 1) + self.fib(n - 2)) % (10 ** 9 + 7)


class Solution:
    """解法三：递归 + 缓存"""

    def fib(self, n: int) -> int:
        memo = [-1] * (n + 1)
        return self._fib(n, memo)

    def _fib(self, n: int, memo: List[int]) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if memo[n] > -1:
            return memo[n]
        memo[n] = (self._fib(n - 1, memo) + self._fib(n - 2, memo)) % (10 ** 9 + 7)
        return memo[n]


if __name__ == "__main__":
    solution = Solution()
    assert solution.fib(2) == 1
    assert solution.fib(5) == 5
