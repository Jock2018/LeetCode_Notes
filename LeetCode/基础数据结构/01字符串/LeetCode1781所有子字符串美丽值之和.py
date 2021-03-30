#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/3/30 23:13
LeetCode原题链接：https://leetcode-cn.com/problems/sum-of-beauty-of-all-substrings/
"""


class Solution:
    """解法一：暴力求解

    两层遍历
    """

    def beautySum(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            counter = {}
            for j in range(i, len(s)):
                counter[s[j]] = counter.get(s[j], 0) + 1
                max_count = max(counter.values())
                min_count = min(counter.values())
                result += max_count - min_count
        return result


if __name__ == "__main__":
    solution = Solution()
    s = "aabcb"
    print(f"预期：5")
    print(f"实际：{solution.beautySum(s)}")
