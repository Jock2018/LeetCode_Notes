#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/19 23:25
LeetCode原题链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
"""


class Solution:
    """动态规划"""

    def translateNum(self, num: int) -> int:
        str_num = str(num)
        n = len(str_num)
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            if str_num[i - 2] == '1' or (str_num[i - 2] == '2' and str_num[i - 1] < '6'):
                dp[i] = dp[i - 2] + dp[i - 1]
            else:
                dp[i] = dp[i - 1]
        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    s = 12258
    print(f"预期：5")
    print(f"实际：{solution.translateNum(s)}")
