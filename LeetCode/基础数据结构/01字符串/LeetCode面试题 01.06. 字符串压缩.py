#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/3/31 0:11
LeetCode原题链接：https://leetcode-cn.com/problems/compress-string-lcci/
"""


class Solution:
    """解法一：遍历一次+引入末尾虚节点"""

    def compressString(self, S: str) -> str:
        result = []
        s = S + "*"
        count = 1
        for i in range(0, len(S)):
            if s[i] != s[i + 1]:
                result.append(s[i])
                result.append(str(count))
                count = 1
            else:
                count += 1
        if len(S) <= len(result):
            return S
        return "".join(result)


if __name__ == "__main__":
    solution = Solution()
    s = "aabcccccaaa"
    print(f"预期：a2b1c5a3")
    print(f"实际：{solution.compressString(s)}")

    solution = Solution()
    s = "abbccd"
    print(f"预期：abbccd")
    print(f"实际：{solution.compressString(s)}")
