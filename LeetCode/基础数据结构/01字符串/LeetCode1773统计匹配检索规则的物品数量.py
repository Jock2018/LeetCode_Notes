#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import List

"""
时间：2021/3/29 23:43
LeetCode原题链接：https://leetcode-cn.com/problems/count-items-matching-a-rule/
"""


class Solution:
    """解法一：构造枚举，遍历一次判断即可

    思路：
    因为总共只有 3 中可能，所以通过 ruleKey 判断出需要用 type, color, name 中的哪一个做筛选，
    然后直接遍历判断即可
    """

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key_type = ("type", "color", "name")
        index = key_type.index(ruleKey)
        result = 0
        for item in items:
            if item[index] == ruleValue:
                result += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    print(f"预期：1")
    print(f"实际：{solution.countMatches(items, ruleKey, ruleValue)}")
