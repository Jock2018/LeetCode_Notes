#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/18 13:31
LeetCode原题链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""


class Solution1:
    """解法一：暴力解循环"""

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        max_length = 0
        char_set = set()
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[j] not in char_set:
                    char_set.add(s[j])
                else:
                    if max_length < len(char_set):
                        max_length = len(char_set)
                    char_set.clear()
                    break
        return max_length


# class Solution:
#     """解法二：滑动窗口"""
#
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         i, j, max_length, char_set = 0, 0, 0, set()
#         while j < len(s):
#             if s[j] not in char_set:
#                 char_set.add(s[j])
#                 j += 1
#             else:
#                 if max_length < len(char_set):
#                     max_length = len(char_set)
#                 while s[i] not in char_set:
#                     char_set.remove(s[i])
#                     i += 1
#                 char_set.remove(s[i])
#                 i += 1
#         if max_length < len(char_set):
#             max_length = len(char_set)
#         return max_length

class Solution:
    """解法二：滑动窗口
    根据官方题解优化，比官方的快近一倍。主要是处理右指针稍微不同。
    右指针到头说明遍历到尾即可终止，不必左指针也到尾。
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, max_length, char_set = 0, 0, 0, set()
        while right < len(s):
            # 不重复则放入集合中，同时右指针向前一步
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
            else:
                # 重复时，需要记录最大值
                if max_length < len(char_set):
                    max_length = len(char_set)
                # 重复时，需要移动左指针到重复字符的位置，并把相关的字符移出集合
                while s[left] != s[right]:
                    char_set.remove(s[left])
                    left += 1
                # 注意，这里保留右指针指向的重复值，左指针指向的需要移出
                char_set.remove(s[left])
                left += 1
        if max_length < len(char_set):
            max_length = len(char_set)
        return max_length


class Solution3:
    """官方解答：非最优，比自己一开始写的慢了一倍"""

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans


# class Solution:
#     """解法四：滑动窗口
#     在 2 和 3 的基础上优化代码
#     """
#
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         i, j, max_length, char_set = 0, 0, 0, set()
#         for j in range(len(s)):
#             if s[j] not in char_set:
#                 char_set.add(s[j])
#                 j += 1
#             else:
#                 # 左指针移动到重复的那个字符，并且把
#                 max_length = max(max_length, len(char_set))
#                 while s[i] not in char_set:
#                     char_set.remove(s[i])
#                     i += 1
#                 char_set.remove(s[i])
#                 i += 1
#         max_length = max(max_length, len(char_set))
#         return max_length


if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    print(f"预期：3")
    assert solution.lengthOfLongestSubstring(s) == 3
    print(f"实际：{solution.lengthOfLongestSubstring(s)}")

    solution = Solution()
    s = "pwwkew"
    print(f"预期：3")
    print(f"实际：{solution.lengthOfLongestSubstring(s)}")

    solution = Solution()
    s = "aa"
    print(f"预期：1")
    print(f"实际：{solution.lengthOfLongestSubstring(s)}")

    solution = Solution()
    s = "a"
    print(f"预期：1")
    print(f"实际：{solution.lengthOfLongestSubstring(s)}")

    solution = Solution()
    s = ""
    print(f"预期：0")
    print(f"实际：{solution.lengthOfLongestSubstring(s)}")
