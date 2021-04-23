#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/23 23:20
LeetCode原题链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/
"""


class MinStack:
    """解题思路：利用数据栈和辅助栈"""

    def __init__(self):
        self.data_stack, self.min_stack = [], []

    def push(self, x: int) -> None:
        self.data_stack.append(x)
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.data_stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.data_stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(f"预期：-3")
    print(f"实际：{min_stack.min()}")
    min_stack.pop()
    print(f"预期：0")
    print(f"实际：{min_stack.top()}")
