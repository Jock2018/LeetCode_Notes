#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/9/13 22:34
LeetCode原题链接：https://leetcode-cn.com/problems/binary-search/
"""
from typing import List


class Solution:
    """解法一：二分查找"""

    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, (len(nums) - 1)
        medium = (low + high) // 2
        while low < high:
            if nums[medium] == target:
                return medium
            if nums[medium] > target:
                high = medium - 1
                medium = (low + high) // 2
            if nums[medium] < target:
                low = medium + 1
                medium = (low + high) // 2
        if low == high and nums[low] == target:
            return low
        return -1


if __name__ == "__main__":
    solution = Solution()
    # assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    # assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert solution.search([5], 5) == 0
