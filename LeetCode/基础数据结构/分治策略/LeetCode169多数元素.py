#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/9/13 23:35
LeetCode原题链接：https://leetcode-cn.com/problems/majority-element/
"""
import collections
from typing import List


# class Solution:
#     """解法一：遍历 + map """
#
#     def majorityElement(self, nums: List[int]) -> int:
#         d = {}
#         times = len(nums) / 2
#         for num in nums:
#             d[num] = d.get(num, 0) + 1
#         for key, value in d.items():
#             if value > times:
#                 return key
#
# class Solution:
#     """解法二：遍历 + map"""
#
#     def majorityElement(self, nums: List[int]) -> int:
#         counts = collections.Counter(nums)
#         return max(counts.keys(), key=counts.get)


# class Solution:
#     """解法三：排序"""
#
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums) // 2]


# class Solution:
#     """解法四：摩尔投票法"""
#
#     def majorityElement(self, nums: List[int]) -> int:
#         cand_num, count = nums[0], 1
#         for num in nums:
#             if num == cand_num:
#                 count += 1
#             else:
#                 count -= 1
#                 if count == 0:
#                     cand_num = num
#                     count = 1
#         return cand_num

class Solution:
    """解法五：分治法"""

    def majorityElement(self, nums: List[int]) -> int:
        return self._devide(nums, 0, len(nums) - 1)

    def _devide(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return nums[left]
        medium = (left + right) // 2
        left_max = self._devide(nums, left, medium)
        right_max = self._devide(nums, medium + 1, right)
        if left_max == right_max:
            return left_max
        left_cnt = self._conquer(nums, left_max, left, right)
        right_cnt = self._conquer(nums, right_max, left, right)
        return left_max if left_cnt > right_cnt else right_max

    def _conquer(self, nums: List[int], target: int, left: int, right: int) -> int:
        count = 0
        for i in (left, right + 1):
            if nums[i] == target:
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    assert solution.majorityElement([3, 2, 3]) == 3
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
