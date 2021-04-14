#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/14 23:07
LeetCode原题链接：https://leetcode-cn.com/problems/valid-palindrome-ii/
"""
from typing import Tuple


class Solution1:
    """解法一：双指针
    思路：
    双指针，收尾开始遍历：
    1. 如果全部相等，则是回文
    2. 第一个不相等的字符，分别去掉左右两个字符，构造两个子串，判断这两个子串中是否有回文，
    有则说明能通过删除 1 个字符变为回文，反之不能
    """

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:
                s1 = s[:i] + s[i + 1:]
                s2 = s[:j] + s[j + 1:]
                strings = (s1, s2)
                if self.has_palindrome(strings):
                    return True
                return False

        return True

    def has_palindrome(self, strings: Tuple[str, str]) -> bool:
        for string in strings:
            i, j = 0, len(string) - 1
            while i < j:
                if string[i] == string[j]:
                    i += 1
                    j -= 1
                    continue
                else:
                    break
            else:
                return True
        return False


class Solution:
    """解法二：在 1 的基础上优化处理，已经判断过的不再判断，参考官方题解"""

    def validPalindrome(self, s: str) -> bool:
        is_palindrome = lambda s: s == s[::-1]
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return is_palindrome(s[left:right]) or is_palindrome(s[left + 1: right + 1])
        return True


if __name__ == "__main__":
    solution = Solution()
    s = "aba"
    print(f"预期：True")
    print(f"实际：{solution.validPalindrome(s)}")

    solution = Solution()
    s = "abca"
    print(f"预期：True")
    print(f"实际：{solution.validPalindrome(s)}")

    solution = Solution()
    s = "abcadef"
    print(f"预期：False")
    print(f"实际：{solution.validPalindrome(s)}")

    solution = Solution()
    s = "aa"
    print(f"预期：True")
    print(f"实际：{solution.validPalindrome(s)}")

    solution = Solution()
    s = "ececabbacec"
    print(f"预期：True")
    print(f"实际：{solution.validPalindrome(s)}")

    solution = Solution()
    s = "ab"
    print(f"预期：True")
    print(f"实际：{solution.validPalindrome(s)}")

    solution = Solution()
    s = "abc"
    print(f"预期：False")
    print(f"实际：{solution.validPalindrome(s)}")
