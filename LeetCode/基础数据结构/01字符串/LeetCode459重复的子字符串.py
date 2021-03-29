#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/3/28 23:00
LeetCode原题链接：https://leetcode-cn.com/problems/repeated-substring-pattern/
"""


class Solution:
    """解法一：两层遍历，枚举

    小优化：因为必须重复因此，所以子串的长度必定在 1-len(s)//2 之间
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            j, k = 0, i
            while len(s[k:]) >= i:
                if s[j:k] == s[k: k + i]:
                    j += i
                    k += i
                    continue
                break

            if len(s[k:]) == 0:
                return True
        return False


class Solution2:
    """解法二官方题解：两层遍历，枚举

    代码比解法一简洁多了
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True
        return False


if __name__ == "__main__":
    solution = Solution()
    s = "abab"
    print(f"预期：True")
    print(f"实际：{solution.repeatedSubstringPattern(s)}")

    solution = Solution()
    s = "abcabcabcabc"
    print(f"预期：True")
    print(f"实际：{solution.repeatedSubstringPattern(s)}")

    solution = Solution()
    s = "babbabbabbabbab"
    print(f"预期：True")
    print(f"实际：{solution.repeatedSubstringPattern(s)}")

    solution = Solution2()
    s = "abab"
    print(f"预期：True")
    print(f"实际：{solution.repeatedSubstringPattern(s)}")

    solution = Solution2()
    s = "abcabcabcabc"
    print(f"预期：True")
    print(f"实际：{solution.repeatedSubstringPattern(s)}")

    solution = Solution2()
    s = "babbabbabbabbab"
    print(f"预期：True")
    print(f"实际：{solution.repeatedSubstringPattern(s)}")

    "abcabc".find("abc", 1)
