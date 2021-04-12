#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/13 0:08
LeetCode原题链接：https://leetcode-cn.com/problems/longest-common-prefix/
"""
from typing import List


class Solution:
    """解法一：迭代暴力解"""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) == 0:
            return result
        if len(strs) == 1:
            return strs[0]
        min_len = len(sorted(strs)[0])
        for i in range(min_len):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return result
            result += strs[j][i]
        return result


if __name__ == "__main__":
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    print(f"预期：'fl'")
    print(f"实际：{solution.longestCommonPrefix(strs)}")

    solution = Solution()
    strs = ["flower", "flower", "flower"]
    print(f"预期：'flower'")
    print(f"实际：{solution.longestCommonPrefix(strs)}")

    solution = Solution()
    strs = ["", "", ""]
    print(f"预期：''")
    print(f"实际：{solution.longestCommonPrefix(strs)}")

    solution = Solution()
    strs = ["a"]
    print(f"预期：'a'")
    print(f"实际：{solution.longestCommonPrefix(strs)}")
