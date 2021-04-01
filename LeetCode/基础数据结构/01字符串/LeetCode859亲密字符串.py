#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/1 0:07
LeetCode原题链接：https://leetcode-cn.com/problems/buddy-strings/
"""


class Solution:
    """解法一：遍历一次即可，重点是找到符合要求的条件

    两种情况是符合要求的：
    1. 只有 2 个位置不同，且这两个位置的字符顺序是交换的，如：abcd, dbca这种情况
    2. 字母都相同，且至少有一个字母有重复，如：aba, aba 这种情况。
    """

    def buddyStrings(self, a: str, b: str) -> bool:
        # 长度不等或长度 < 2 肯定不满足要求
        if len(a) != len(b) or len(a) < 2 or len(b) < 2:
            return False
        # flag 用于判断是否有重复字母，count 记录索引相同字母不同的索引个数
        flag, count = False, 0
        chars = set()
        # j 用于记录第一次字母不同的索引
        j = -1
        for i in range(len(a)):
            if a[i] not in chars:
                chars.add(a[i])
            else:
                flag = True

            if a[i] != b[i]:
                # 有超过 2 个位置不同，则返回 False
                count += 1
                if count > 2:
                    return False
                # 第一次不同，则把两个字母暂存，后面使用
                if j == -1:
                    j = i
                else:
                    if a[j] != b[i] or b[j] != a[i]:
                        return False
        if count == 2 or (count == 0 and flag):
            return True
        return False


if __name__ == "__main__":
    solution = Solution()
    A = "ab"
    B = "ba"
    print(f"预期：True")
    print(f"实际：{solution.buddyStrings(A, B)}")
