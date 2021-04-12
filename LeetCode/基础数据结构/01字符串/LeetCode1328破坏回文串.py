#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/1 23:06
LeetCode原题链接：https://leetcode-cn.com/problems/break-a-palindrome/
"""


class Solution:
    """解法一：贪心
    前面的能换成'a'，就换。
    若全是'a'，末位换成‘b’
    """

    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        result = list(palindrome)
        # 回文，所以取一半即可，找到第一个不为 a 的替换为 a，即为答案
        for i in range(len(result) // 2):
            if result[i] != "a":
                result[i] = "a"
                return "".join(result)
        # 如果前面全是 a，说明前面全是 a，这时把 最后一个字符变为 b 即可
        result[-1] = "b"
        return "".join(result)


if __name__ == "__main__":
    solution = Solution()
    palindrome = "abccba"
    print(f"预期：aaccba")
    print(f"实际：{solution.breakPalindrome(palindrome)}")

    solution = Solution()
    palindrome = "a"
    print(f"预期：''")
    print(f"实际：{solution.breakPalindrome(palindrome)}")

    solution = Solution()
    palindrome = "aa"
    print(f"预期：ab")
    print(f"实际：{solution.breakPalindrome(palindrome)}")

    solution = Solution()
    palindrome = "aba"
    print(f"预期：abb")
    print(f"实际：{solution.breakPalindrome(palindrome)}")

    solution = Solution()
    palindrome = "aaaa"
    print(f"预期：aaab")
    print(f"实际：{solution.breakPalindrome(palindrome)}")

    solution = Solution()
    palindrome = "abba"
    print(f"预期：aaba")
    print(f"实际：{solution.breakPalindrome(palindrome)}")
