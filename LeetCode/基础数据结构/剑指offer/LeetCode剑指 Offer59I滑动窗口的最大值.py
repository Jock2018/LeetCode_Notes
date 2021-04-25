#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/25 22:38
LeetCode原题链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/
"""
from typing import List


class Solution1:
    """暴力解"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 1:
            return nums
        left, right, result = 0, k, []
        while right <= len(nums):
            max_num = max(nums[left: right])
            result.append(max_num)
            left += 1
            right += 1
        return result


class Solution:
    """暴力解"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1 or k == 1:
            return nums
        left, right, = 1, k
        max_num, result = max(nums[:k]), []
        result.append(max_num)
        while right < len(nums):
            if nums[right] > max_num:
                max_num = nums[right]
            elif nums[left] == max_num:
                max_num = max(nums[left:right])
            result.append(max_num)
            right += 1
            left += 1
        return result


if __name__ == "__main__":
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3
    # solution = Solution()
    # print(f"预期：[3, 3, 5, 5, 6, 7]")
    # print(f"实际：{solution.maxSlidingWindow(nums, k)}")
    #
    # # 为空
    # nums = []
    # k = 0
    # solution = Solution()
    # print(f"预期：[]")
    # print(f"实际：{solution.maxSlidingWindow(nums, k)}")
    #
    # # 为 1
    # nums = [1]
    # k = 1
    # solution = Solution()
    # print(f"预期：[1]")
    # print(f"实际：{solution.maxSlidingWindow(nums, k)}")
    #
    # # 为 2
    # nums = [1, -1]
    # k = 1
    # solution = Solution()
    # print(f"预期：[1, -1]")
    # print(f"实际：{solution.maxSlidingWindow(nums, k)}")

    # 为 3
    nums = [7, 2, 4]
    k = 2
    solution = Solution()
    print(f"预期：[7, 4]")
    print(f"实际：{solution.maxSlidingWindow(nums, k)}")
