#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/12 23:49
LeetCode原题链接：https://leetcode-cn.com/problems/valid-palindrome/
"""


class Solution:
    """解法一：双指针法"""

    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        if len(s) == 0:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    print(f"预期：True")
    print(f"实际：{solution.isPalindrome(s)}")
