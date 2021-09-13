#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/9/13 23:18
LeetCode原题链接：https://leetcode-cn.com/problems/recursive-mulitply-lcci/
"""


class Solution:
    """累加处理"""

    def multiply(self, A: int, B: int) -> int:
        if 0 in (A, B):
            return 0
        total = 0
        A, B = min(A, B), max(A, B)
        while A:
            total += B
            A -= 1
        return total


if __name__ == "__main__":
    solution = Solution()
    assert solution.multiply(1, 10) == 10
    assert solution.multiply(3, 4) == 12
