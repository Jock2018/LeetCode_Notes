#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/20 23:35
LeetCode原题链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
"""


class Solution:
    """遍历替换"""

    def replaceSpace(self, s: str) -> str:
        result = []
        for char in s:
            if char == " ":
                result.append("%20")
            else:
                result.append(char)
        return "".join(result)


if __name__ == "__main__":
    solution = Solution()
    s = "We are happy."
    print(f"预期：We%20are%20happy.")
    print(f"实际：{solution.replaceSpace(s)}")
