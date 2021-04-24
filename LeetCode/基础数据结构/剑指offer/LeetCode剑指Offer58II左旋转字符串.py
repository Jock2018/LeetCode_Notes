#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/24 12:00
LeetCode原题链接：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
"""


class Solution:
    """Python 特性解决即可"""
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


if __name__ == "__main__":
    s, k = "abcdefg", 2
    solution = Solution()
    print(f"预期：cdefgab")
    print(f"实际：{solution.reverseLeftWords(s, k)}")
