#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/3/29 23:19
LeetCode原题链接：https://leetcode-cn.com/problems/increasing-decreasing-string/
"""


class Solution:
    """解法一：不断的遍历 a-z

    思路：
    直接翻译题目，a-z z-a 不断地重复，直至 s 为空
    """
    def sortString(self, s: str) -> str:
        alpha_list = [chr(i) for i in range(97, 123)]
        input_alpha = list(s)
        result = []
        while input_alpha:
            for alpha in alpha_list:
                if alpha in input_alpha:
                    result.append(alpha)
                    input_alpha.remove(alpha)
            for alpha in alpha_list[::-1]:
                if alpha in input_alpha:
                    result.append(alpha)
                    input_alpha.remove(alpha)
        return "".join(result)


class Solution2:
    """解法二：桶计数

    思路：
    1. 遍历一遍字母，进行计数
    2. 来回遍历 0-25 即 a-z，直至所有的计数为 0
    """

    def sortString(self, s: str) -> str:
        alpha_count = [0] * 26
        for alpha in s:
            alpha_count[ord(alpha) - ord("a")] += 1
        result = []
        while len(result) < len(s):
            for i in range(0, 26):
                if alpha_count[i] != 0:
                    result.append(chr(i+ord("a")))
                    alpha_count[i] -= 1
            for i in range(25, -1, -1):
                if alpha_count[i] != 0:
                    result.append(chr(i + ord("a")))
                    alpha_count[i] -= 1
        return "".join(result)


if __name__ == "__main__":
    solution = Solution()
    s = "aaaabbbbcccc"
    print(f"预期：abccbaabccba")
    print(f"实际：{solution.sortString(s)}")

    solution = Solution()
    s = "leetcode"
    print(f"预期：cdelotee")
    print(f"实际：{solution.sortString(s)}")

    solution = Solution2()
    s = "aaaabbbbcccc"
    print(f"预期：abccbaabccba")
    print(f"实际：{solution.sortString(s)}")

    solution = Solution2()
    s = "leetcode"
    print(f"预期：cdelotee")
    print(f"实际：{solution.sortString(s)}")

