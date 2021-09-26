#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/9/22 8:25
LeetCode原题链接：https://leetcode-cn.com/problems/XagZNi/
"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """解法一：栈"""
        stack, index = [], 0
        length = len(asteroids)
        while index < length:
            if not stack or stack[-1] < 0 or asteroids[index] > 0:
                stack.append(asteroids[index])
            elif stack[-1] <= -asteroids[index]:
                if stack.pop() < -asteroids[index]:
                    continue
            index += 1
        return stack


if __name__ == "__main__":
    solution = Solution()
    assert solution.asteroidCollision([5, 10, -5]) == [5, 10]
