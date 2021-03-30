#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/3/31 0:35
LeetCode原题链接：https://leetcode-cn.com/problems/generate-a-string-with-characters-that-have-odd-counts/
"""


class Solution:
    """解法一：奇不变，偶减一，字符换拼接"""

    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return "a" * n
        return "a" * (n - 1) + "b"


if __name__ == "__main__":
    solution = Solution()
    n = 4
    print(f"预期：aaab")
    print(f"实际：{solution.generateTheString(n)}")
